#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__      = "Ricardo Ribeiro"
__credits__     = ["Ricardo Ribeiro"]
__license__     = "MIT"
__version__     = "0.0"
__maintainer__  = "Ricardo Ribeiro"
__email__       = "ricardojvr@gmail.com"
__status__      = "Development"


from setuptools import setup

setup(

	name				='Modular computer vision API',
	version 			='0.0',
	description 		="""""",
	author  			='Ricardo Ribeiro',
	author_email		='ricardojvr@gmail.com',
	license 			='MIT',

	packages=[
		'mcv_api',
		'mcv_api.filters',
		'mcv_api.blobs.specialized',
		'mcv_api.blobs.specialized.flies',
		'mcv_api.blobs.specialized.mice',
		],
)