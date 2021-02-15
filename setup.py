from setuptools import setup

DISTNAME = 'ksmith'

VERSION= '0.0.01'

DESCRIPTION = "Kent Smith's personnal python library."

LICENSE = 'MIT'

URL='https://github.com/mehismyname/Ksmith.git'

AUTHOR = "Kent Smith"

KEYWORDS = ['ksmith']

REQUIREMENTS = []

PYTHON = ">= 3.5"

setup(name=DISTNAME,
	packages=['ksmith'],
	package_dir={'ksmith':'module/ksmith'},
	version=VERSION,
	description=DESCRIPTION,
	lincense=LICENSE,
	author=AUTHOR,
	url=URL,
	keywords=KEYWORDS,
	install_requires=REQUIREMENTS,
	python_requires=PYTHON,)