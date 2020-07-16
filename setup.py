# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpnext_operations/__init__.py
from erpnext_operations import __version__ as version

setup(
	name='erpnext_operations',
	version=version,
	description='Create invoices, manage meter readings, manage fuel prices, etc...',
	author='frappe',
	author_email='itsupport@enerwhere.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
