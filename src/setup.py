from distutils.core import setup

setup(name='pytoggl',
      version='0.2',
      description='Python Toggl REST API Wrapper',
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      #url='http://www.python.org/sigs/distutils-sig/',
      packages=['pytoggl', 'pytoggl.api', 'pytoggl.model'],
     )