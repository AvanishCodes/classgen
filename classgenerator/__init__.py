from sys import modules
from .classgenerator import ClassGenerator


# export the ClassGenerator class
modules['__all__'] = ['ClassGenerator']
modules['__dict__'] = {
    'ClassGenerator': ClassGenerator
}
modules['name'] = 'ClassGenerator'
modules['author'] = 'Avanish Gupta'