"""
Flask-MyAdmin
------
A Simple Extension for Mysql Web Mangement

"""
from setuptools import setup


setup(
    name='Flask-MyAdmin',
    version='1.0',
    url='http://github.com/atulmishra-one/flask-myadmin',
    license='BSD',
    author='atul mishra',
    author_email='atulmishra-one@example.com',
    description='A Simple Extension for Mysql Web Management',
    long_description=__doc__,
    packages=['flask_myadmin'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
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