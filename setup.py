from setuptools import setup, find_packages

setup(
    name="mauttos-randtools",
    version="1.0.0",
    author="Marcos Valério Battisti",
    author_email="sinhozinhotarantino@gmail.com",
    description="Advanced random number list generation library.",
    long_description="Biblioteca matemática criada para ensino e engenharia de sistemas.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)