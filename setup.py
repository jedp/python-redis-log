
try:
    from setuptools import setup
except ImportError:
    from distutils import setup
    
setup(
      name='python-redis-log',
      version='0.0.1',
      description='Redis pub/sub logging handler for python',
      author='Jed Parsons',
      author_email='jed@jedparsons.com',
      url='git://github.com/jedp/python-redis-log.git',
      packages=['redislog'],
      install_requires=['redis', 'simplejson']
)
