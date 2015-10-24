"""
Flask-Casl
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='flask_casl',
    version='1.0',
    url='http://alpheios.net/flask-casl/',
    license='GNU GPL'
    author='Your Name',
    author_email='balmas@gmail.com',
    description='flask wrapper for casl',
    long_description=__doc__,
    #py_modules=['flask_casl'],
    packages = find_packages(exclude=["examples"]),
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    tests_require=[
        "mock==1.0.1"
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
