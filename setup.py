import pathlib
from setuptools import setup, find_packages


base_packages = []

docs_packages = [
    "mkdocs>=1.2.3",
    "mkdocs-material==8.1.3",
    "mkdocstrings>=0.17.0",
    "mktestdocs==0.1.2",
    "pygments>=2.10",
    "pymdown-extensions>=9.0",
]

test_packages = [
    "interrogate>=1.5.0",
    "flake8>=3.6.0",
    "pytest>=4.0.2",
    "black>=19.3b0",
    "pre-commit>=2.2.0",
    "flake8-print>=4.0.0",
]

build_packages = [
    "twine",
    "setuptools",
    "build",
]

all_packages = base_packages
dev_packages = all_packages + docs_packages + test_packages + build_packages


setup(
    name="genespeak",
    version="0.0.1",
    author="Sugato Ray",
    packages=find_packages(exclude=["notebooks", "docs"]),
    description="A library to encode text as DNA and decode DNA to text.",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://sugatoray.github.io/genespeak/",
    project_urls={
        "Documentation": "https://sugatoray.github.io/genespeak/",
        "Source Code": "https://github.com/sugatoray/genespeak/",
        "Issue Tracker": "https://github.com/sugatoray/genespeak/issues",
    },
    install_requires=base_packages,
    extras_require={"dev": dev_packages},
    license_files=("LICENSE",),
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
    ],
)
