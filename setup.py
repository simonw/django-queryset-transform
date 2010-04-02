from distutils.core import setup
import os

setup(
    name = 'django-queryset-transform',
    packages = ['queryset_transform'],
    version='0.0.1',
    description='Experimental .transform(fn) method for Django QuerySets, for '
                'clever lazily evaluated optimisations.',
    long_description=open('README.txt').read(),
    author='Simon Willison',
    author_email='simon@simonwillison.net',
    url='http://github.com/simonw/django-queryset-transform',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
