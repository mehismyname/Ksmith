from setuptools import setup

DISTNAME = 'ksmith'

VERSION= '0.0.3'

DESCRIPTION = "Kent Smith's personnal python library."

LONG_DESCRIPTION = "My personal library"

LICENSE = 'MIT'

URL='https://github.com/mehismyname/Ksmith'

AUTHOR = "Kent Smith"

EMAIL= "no-reply@gmail.com"

KEYWORDS = ['ksmith']

REQUIREMENTS = []

PYTHON = ">= 3.5"

setup(name=DISTNAME,
	packages=['ksmith'],
	package_dir={'ksmith':'module/ksmith'},
	version=VERSION,
	description=DESCRIPTION,
	long_description=LONG_DESCRIPTION,
	license=LICENSE,
	author=AUTHOR,
	url=URL,
	keywords=KEYWORDS,
	install_requires=REQUIREMENTS,
	python_requires=PYTHON,)