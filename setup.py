from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="node-tasks-michalStarski",
    version="0.0.1",
    author="Michał Starski",
    author_email="michal.starski@pm.me",
    description="Simple CLI script for listing and running npm/yarn tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michalStarski/node-tasks",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    install_requires=[
        'iterfzf'
    ],
    license='MIT',
    entry_points={
        'console_scripts': [
            'nodetasks=nodetasks:main'
        ]
    }
)
