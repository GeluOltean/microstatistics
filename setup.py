from setuptools import setup, find_packages

setup(
	name='microstatistics',
	packages=find_packages(),
	version='0.5.5',
	description='A package for micropalaeontological statisics with a Qt5 ' +
	'gui. Launched with microstatistics-start. Requires installation through '+
	'pip3.',
	author='Gelu Oltean',
	author_email='geluoltean8@gmail.com',
	url='https://github.com/GeluOltean/microstatistics',
	license='GNU GPL 3',
	install_requires=['PyQt5', 'scipy', 'matplotlib', 'numpy', 'pandas',
	'scipy', 'sklearn', 'xlrd'],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: X11 Applications :: Qt',
		'Environment :: Console',
		'Operating System :: OS Independent',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Programming Language :: Python :: 3.6',],
	script=['microstatistics/microstatistics-start'],
	entry_points={
		'console_scripts': [
			'microstatistics-start = microstatistics.command_line:main'
		]},
)
