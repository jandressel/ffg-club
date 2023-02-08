from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ffg/__init__.py
from ffg import __version__ as version

setup(
	name="ffg",
	version=version,
	description="Frappe Framework Gym Club",
	author="Dressel",
	author_email="jan@dressel.cloud",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
