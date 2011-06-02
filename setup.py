try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os import path

README = path.abspath(path.join(path.dirname(__file__), 'README.rst'))

setup(
      name='python-redis-log',
      version='0.1.2',
      description='Redis pub/sub logging handler for python',
      long_description=open(README).read(),
      author='Jed Parsons',
      author_email='jed@jedparsons.com',
      url='https://github.com/jedp/python-redis-log',
      packages=['redislog'],
      license='MIT',
      install_requires=['redis', 'simplejson']
)
