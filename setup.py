import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

with open("./README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="medcat",
    version="1.1.3",
    author="w-is-h",
    author_email="w.kraljevic@gmail.com",
    description="Concept annotation tool for Electronic Health Records",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CogStack/MedCAT",
    packages=['medcat', 'medcat.utils', 'medcat.preprocessing', 'medcat.cogstack', 'medcat.ner', 'medcat.linking', 'medcat.datasets', 'medcat.deprecated', 'medcat.cli'],
    install_requires=[
        'numpy<1.21.0,>=1.19.0',
        'pandas~=1.0',
        'gensim~=3.8',
        'spacy<3.1.0',
        'scipy~=1.5',
        'transformers~=4.5.1',
        'torch~=1.8.1',
        'tqdm<4.50.0,>=4.27',
        'sklearn~=0.0',
        'elasticsearch~=7.10',
        'dill~=0.3.4',
        'datasets~=1.6.0',
        'gitpython~=3.1.17',
        'pydrive2~=1.8.3',
        'dvc~=2.6.4',
        'fire~=0.4.0',
        'wexpect~=4.0.0',
        'pexpect~=4.8.0',
        'jsonpickle~=2.0.0'
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
