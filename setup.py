from setuptools import setup, find_packages
from os.path import join, dirname

#import http_cats

setup(name='http_cats',
      version='1.0',
      packages=find_packages(),
      long_description=open(join(dirname(__file__), 'README.md')).read(),
      include_package_data=True,
      install_requires=[
            'certifi==2020.6.20',
            'chardet==3.0.4',
            'idna==2.10',
            'requests==2.24.0',
            'urllib3==1.25.10',
        ],
      )