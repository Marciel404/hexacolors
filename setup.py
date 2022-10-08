from setuptools import setup

with open("README.md", "r") as f:

    long_description = f.read()

setup(
    name="hexacolors",
    version="0.3.5",
    url = 'https://github.com/Marciel404/hexacolors',
    author="Marciel404",
    description="Convert string color for hexadecimal understandable by python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["hexacolors","hexacolors.colors"],
    license = 'MIT',
    keywords = 'String to hexadecimal color converter' ,
    CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ],
    python_requires='>=3.8',
    install_requires=['requests>=2.28.1'],
    dependency_links=['https://github.com/Marciel404/hexacolors']
)