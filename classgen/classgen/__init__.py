from sys import modules
from .ClassGenerator import ClassGenerator

# Export the ClassGenerator class
modules['__all__'] = ['ClassGenerator']
modules['name'] = 'ClassGenerator'
modules['author'] = 'Avanish Gupta'