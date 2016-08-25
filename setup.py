from setuptools import setup

setup(
    name='django-jux',
    version='1.1',
    description='JUnit-style XML output for Django tests',
    author='Sean Myers',
    author_email='sean.dst@gmail.com',
    url='https://bitbucket.org/seandst/django-jux',
    packages=['juxd'],
    license='MIT Expat License',
    long_description=open('README.rst').read(),
    install_requires=[
        'Django >= 1.6',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: DFSG approved',
        'License :: Freely Distributable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Testing',
    ]
)
