from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='aux',
      version=version,
      description="Automation Framework",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='TestCase Automation Device Network Protocol',
      author='email@protojour.com',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'unittest2',
        'lxml',
        'nose',
        'sphinx',
        'Fabric',
        'Werkzeug',
        'colorama',
      ],
      entry_points={
        'console_scripts': [
            'aux = aux:run',
        ]},
      
      )
