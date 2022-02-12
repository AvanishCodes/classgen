# Class Generator tool

## Generate class files in Python using command line arguments

Example:

> `python3 -m classgenerator ClassName member1,member2,member3`

## Following is in the development phase

### Generate class files in Python using a script

```from classgen import ClassGenerator
cg = ClassGenerator('ClassName', ['member1', 'member2'], ['member1', 'member2'])
cg.Generate()
```
