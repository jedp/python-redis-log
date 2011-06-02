try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
      name='python-redis-log',
      version='0.1.1',
      description='Redis pub/sub logging handler for python',
      author='Jed Parsons',
      author_email='jed@jedparsons.com',
      url='https://github.com/jedp/python-redis-log',
      packages=['redislog'],
      license='MIT',
      install_requires=['redis', 'simplejson']
)
