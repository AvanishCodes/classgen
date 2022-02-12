from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="classgen",                            # This is the name of the package
    version="0.0.6",                            # The initial release version
    author="Avanish Gupta",                     # Full name of the author
    description="Generate classes in Python using command line arguments",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                       # Information to filter the project on PyPi website
    python_requires='>=3.6',                 # Minimum version requirement of the package
    py_modules=["classgen"],                 # Name of the python package
    install_requires=[],                     # Install other dependencies if any
    keywords=['Class', 'generate', 'automation', 'command line arguments', 'cli'],
    # package_dir={'':'classgenerator'},     # Directory of the source code of the package
)