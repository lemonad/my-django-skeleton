import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "my-django-skeleton",
    version = "0.1",
    url = 'http://github.com/lemonad/my-django-skeleton',
    license = 'BSD',
    description = "A skeleton setup for starting a django project with virtualenv and buildout.",
    long_description = read('README'),

    author = 'Jonas Nockert',
    author_email = 'jonasnockert@gmail.com',

    packages = find_packages('src'),
    package_dir = {'': 'src'},

    install_requires = ['setuptools'],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
