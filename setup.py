from setuptools import setup

setup(
    name='django-jux',
    version='1.0',
    description='JUnit-style XML output for Django tests',
    author='Sean Myers',
    author_email='sean.dst@gmail.com',
    url='https://bitbucket.org/seandst/django-jux',
    packages=['juxd'],
    license='LICENSE.txt',
    long_description=open('README.rst').read(),
    install_requires=[
        "Django >= 1.3",
    ],
)
