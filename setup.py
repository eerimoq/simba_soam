from setuptools import setup
import re


def find_version():
    return re.search(r"^__version__ = '(.*)'$",
                     open('simba_soam/__init__.py', 'r').read(),
                     re.MULTILINE).group(1)

setup(name='bincopy',
      version=find_version(),
      description=('Simba SOAM.'),
      long_description=open('README.md', 'r').read(),
      author='Erik Moqvist',
      author_email='erik.moqvist@gmail.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.13',
      ],
      keywords=[],
      url='https://github.com/eerimoq/simba_soam',
      py_modules=['simba_soam'],
      install_requires=[],
      python_requires='>=3.9',
      entry_points = {
          'console_scripts': ['simba_soam=simba_soam:_main']
      })
