import os

class ClassGenerator():
    '''
    ClassGenerator
    This class is used to generate a class file.
    
    Params:
        name: The name of the class.
        members: A list of members to be added to the class.
        methods: A list of methods to be added to the class.
        constructor: The name of the constructor.
        constructor_args: A list of arguments to be passed to the constructor.

    Returns:
        None
    '''
    name: str
    members: list()
    getters = list()
    setters = list()
    constructor: str
    constructor_args: list()

    def __init__(self, name: str, members: list(), constructor_args: list()):
        '''
        __init__
        Initializes the class generator.
        
        Params:
            name: The name of the class.
            members: A list of members to be added to the class.
            constructor: The name of the constructor.
            constructor_args: A list of arguments to be passed to the constructor.

        Returns:
            None
        '''
        self.name = name
        self.members = members
        self.constructor_args = constructor_args
        # Create the getters and setters
        for member in members:
            self.getters.append('get_' + member[0] + member[1:])
            self.setters.append('set_' + member[0] + member[1:])
        # Add the constructor

    def generate_class_docstring(self):
        '''
        Generate the class docstring.
        '''
        docstring = str()
        # Create the docstring
        docstring += ('\t\"\"\"\n')
        docstring += ('\tThis class is used to represent a ' + self.name + '.\n')
        # Write details of attributes
        docstring += ('\t\n')
        docstring += ('\tAttributes:\n')
        for member in self.members:
            docstring += ('\t\t' + member + ': The ' + member + ' of the ' + self.name + '.\n')
        docstring += ('\t\n')
        
        # Write details of methods
        docstring += ('\tMethods:\n')
        for getter in self.getters:
            docstring += ('\t\t' + getter + '(self): Gets the ' + getter + ' of the ' + self.name + '.\n')
        for setter in self.setters:
            docstring += ('\t\t' + setter + '(self, ' + setter[4:] + ')' +  ': Sets the ' + setter[4:] + ' of the ' + self.name + '.\n')        
        docstring += ('\t\"\"\"\n')
        docstring += ('\n')
        return docstring

    def generate_members(self):
        '''
        Generate the members docstring.
        '''
        docstring = str()
        # Create the members
        for member in self.members:
            docstring += ('\t_' + member + ': ' + 'None\n')
        docstring += "\t\n"
        return docstring

    def generate_constructor_docstring(self):
        '''
        Generate the constructor docstring.
        '''
        docstring = str()
        # Create the docstring
        docstring += ('\t\t\"\"\"\n')
        docstring += ('\t\tInitializes a ' + self.name + ' object.\n')
        docstring += ('\t\t\n')
        docstring += ('\t\tParams:\n')
        for arg in self.constructor_args:
            docstring += ('\t\t\t' + arg + ': The ' + arg + ' of the ' + self.name + '.\n')
        docstring += ('\t\t\"\"\"\n')
        return docstring

    def generate_constructor(self):
        # Write the constructor
        docstring = str()
        docstring += ('\tdef __init__(self')
        for arg in self.constructor_args:
            docstring += (', ' + arg)
        docstring += ('):\n')
        docstring += (self.generate_constructor_docstring())
        # Write the constructor body
        for member in self.members:
            docstring += ('\t\tself._' + member + ' = ' + member + '\n')
        docstring += ('\t\n')
        return docstring
    
    def generate_getter_docstring(self, member):
        '''
        Generate the getter methods' docstrings.
        '''
        docstring = str()
        # Create the docstring
        docstring += ('\t\t\"\"\"\n')
        docstring += ('\t\tGets the ' + member[4:] + ' of the ' + self.name + '.\n')
        docstring += ('\t\t\n')
        docstring += ('\t\tReturns:\n')
        docstring += ('\t\t\t' + member + ': The ' + member[4:] + ' of the ' + self.name + '.\n')
        docstring += ('\t\t\"\"\"\n')
        return docstring

    def generate_getter(self):
        # Write the getters and setters
        docstring = str()
        for getter in self.getters:
            docstring += ('\tdef ' + getter + '(self):\n')
            docstring += (self.generate_getter_docstring(getter))
            docstring += ('\t\treturn self.' + getter[3:] + '\n')
            docstring += ('\n')
        return docstring
    
    def generate_setter_docstring(self, member):
        '''
        Generate the setter methods' docstrings.
        '''
        docstring = str()
        # Create the docstring
        docstring += ('\t\t\"\"\"\n')
        docstring += ('\t\tSets the ' + member[4:] + ' of the ' + self.name + '.\n')
        docstring += ("\t\t\n")
        docstring += ('\t\tParams:\n')
        docstring += ('\t\t\t' + member[4:] + ': The ' + member[4:] + ' of the ' + self.name + '.\n')
        docstring += ('\t\t\"\"\"\n')
        return docstring

    def generate_setter(self):
        docstring = str()
        for setter in self.setters:
            docstring += ('\tdef ' + setter + '(self, ' + setter[4:] + '):\n')
            docstring += (self.generate_setter_docstring(setter))
            docstring += ('\t\tself.' + setter[3:] + ' = ' + setter[4:] + '\n')
            docstring += ('\n')
            continue
        return docstring

    def generate(self, path: str="./name.py"):
        '''
        generate
        Generates the class file along with docstrings.
        
        Params:
            path: The path to the class file.

        Returns:
            None
        '''
        # Name resolution of the file
        if path == "./name.py":
            path = "./" + self.name + ".py"
        # If file exists, delete the file
        if os.path.exists(path):
            os.remove(path)
        # Create the file
        file = open(path, 'w')
        # Write the class header
        file.write(f'#(class) {self.name}\n')
        file.write('class ' + self.name + ':\n')
        file.write(self.generate_class_docstring())                
        file.write(self.generate_members())
        file.write(self.generate_constructor())
        file.write(self.generate_getter())
        file.write(self.generate_setter())        
        # Close the file
        file.close()
        return None