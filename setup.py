from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'covid19-tracker',
    version = '0.0.4',
    author="Ajay Lingayat",
    author_email="lingayatajay2810@gmail.com",
    description = "This module helps to track Covid19.",
    url="https://github.com/Ajay2810-hub/covid19-tracker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules = ['covid19tracker'],
    package_dir = {'': 'src'},
    install_requires=[
       "bs4",
       "requests",
       "regex",
    ], 
    extras_require = {
       "dev":[
       "pytest>=3.7",
       ]
    },
    classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
