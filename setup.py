from setuptools import setup, find_packages

setup(
    author='Narmina Yadullayeva',
    description='Data Scientist Toolkit',
    name='dstoolkit',
    verion='0.1.0',
    packages=find_packages(include=["dstoolkit","dstoolkit.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)