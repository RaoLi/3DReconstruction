try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = [
	'description': 'This is a demo for 3D reconstruction in Python2.7.11',
	'author':'Rao Li',
	'url' = 'http://github.com/RaoLi/3DReconstruction',
	'download_url':'http://github.com/RaoLi/3DReconstruction',
	'author_email':'seuraoli@gmail.com.',
	'version': '0.1',
	'install_requires':['nose'],
	'packages':['3DReconstruction'],
	'scripts':[],
	'name':'3DReconstruction'
]

setup(**config)