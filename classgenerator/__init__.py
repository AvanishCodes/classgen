from sys import modules
from .classgenerator import ClassGenerator
from argparse import ArgumentParser

# Command line arguments
parser = ArgumentParser(description='Generate a class file.')
parser.add_argument(
    'className', 
    type=str, 
    help='The name of the class.'
)
parser.add_argument(
    'members', 
    type=str, 
    help='The members of the class.'
)
args = parser.parse_args()
if type(args.className) == str:
    cg = ClassGenerator(
        args.className,
        args.members.split(','),
        args.members.split(',')
    )
    cg.generate()
    print(f'Class {args.className} generated successfully.')
else:
    print('Error: Please follow the convention of the command line arguments.')
    print('Example: python3 ClassGenerator Student marks,grade,address')

# export the ClassGenerator class
modules['__all__'] = ['ClassGenerator']
modules['__dict__'] = {
    'ClassGenerator': ClassGenerator
}
modules['name'] = 'ClassGenerator'
modules['author'] = 'Avanish Gupta'