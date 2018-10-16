import os
import sys

from setuptools import setup, find_packages

long_description = 'Please see our GitHub README'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()


def getRequires():
    deps = ['github3.py',
            'requests',
            'beautifulsoup4',
            'sendgrid',
            'python-dateutil',
            'sqlalchemy',
            'datetime',
            'pyyaml',
            'six',
            'wheel',
            'zope.interface',
            'uritemplate',
            'uritemplate.py',
            'pytz',
            'python-http-client']
    if sys.version_info.major >= 3:
        deps.append('pymysql')
    return deps


base_url = 'https://github.com/sendgrid/'
setup(
    name='open_source_library_data_collector',
    version='1.1.0',
    author='Elmer Thomas',
    author_email='dx@sendgrid.com',
    url=base_url + 'open-source-library-data-collector',
    packages=find_packages(),
    license='MIT',
    description='Periodically capture external data relating to GitHub hosted '
                'Open Source libraries',
    long_description=long_description,
    install_requires=getRequires(),
    keywords=[
        'GitHub',
        'Open Source',
        'ROI',
        'Reporting',
        'Package Managers'
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
        'Programming Language :: Python :: 3.6'
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        'console_scripts': ['osscollect=cli:cli'],
    },
)
