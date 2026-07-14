from setuptools import setup
import re


def find_version():
    return re.search(r"^__version__ = '(.*)'$",
                     open('simba_soam/soam.py', 'r').read(),
                     re.MULTILINE).group(1)

setup(name='simba_soam',
      version=find_version(),
      description=('Simba SOAM.'),
      long_description=open('README.md', 'r').read(),
      author='Erik Moqvist',
      author_email='erik.moqvist@gmail.com',
      license='MIT',
      classifiers=[
          'Programming Language :: Python :: 3.9',
      ],
      keywords=[],
      url='https://github.com/eerimoq/simba_soam',
      py_modules=['simba_soam'],
      install_requires=[
          'prompt_toolkit',
          'pyserial'
      ],
      python_requires='>=3.9')
