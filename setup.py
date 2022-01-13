import re
import pathlib
from setuptools import setup, find_packages


BANNER_PATH_PAT = r"\[\#repo-banner\]\:\s+(?P<path>.*)\s*\n"
BANNER_PATH_PAT = re.compile(BANNER_PATH_PAT)
CONTENT_PATH_PREFIX = r"https://raw.githubusercontent.com/sugatoray/genespeak/master/"


def update_banner_path(readme_path: str = "README.md") -> str:
    """Converts the relative path of the banner into a parmalink.

    The banner is made avilable in the readme file as follows:

    --------------------------------------------------------------

    ![genespeak-banner][#repo-banner]

    [#repo-banner]: docs/assets/images/genespeak_banner_01.png

    --------------------------------------------------------------

    This function replaces the target line's <path> value ([#repo-banner]: <path>)
    with CONTENT_PATH_PREFIX + <path>.

    CONTENT_PATH_PREFIX = r"https://raw.githubusercontent.com/sugatoray/genespeak/master/"

    """

    text = pathlib.Path("README.md").read_text()
    res = BANNER_PATH_PAT.search(text)
    replace_with = r"[#repo-banner]: " + CONTENT_PATH_PREFIX + res.groupdict().get("path") + '\n\n'
    mod_text = BANNER_PATH_PAT.sub(replace_with, text)

    return mod_text

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
    "flake8>=4.0.1",
    "pytest>=6.2.5",
    "black>=21.12b0",
    "pre-commit>=2.16.0",
    "pre-commit-hooks>=4.0.0"
    "flake8-print>=4.0.0",
    "flake8-black>=0.2.3",
]

build_packages = [
    "twine",
    "setuptools",
    "build",
    "pkginfo>=1.8.2",
]

all_packages = base_packages
dev_packages = all_packages + docs_packages + test_packages + build_packages


README: str = update_banner_path(readme_path="README.md")

setup(
    name="genespeak",
    version="0.0.8",
    author="Sugato Ray",
    author_email='sugatoray.dev@gmail.com',
    python_requires='>=3.6',
    keywords="genespeak encoding decoding text-to-dna dna-to-text",
    packages=find_packages(
        include = ["genespeak"],
        exclude = ["notebooks", "docs", "test*"]
    ),
    description="A library to encode text as DNA and decode DNA to text.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sugatoray/genespeak/",
    project_urls={
        "Documentation": "https://sugatoray.github.io/genespeak/",
        "Source Code": "https://github.com/sugatoray/genespeak/",
        "Issue Tracker": "https://github.com/sugatoray/genespeak/issues",
    },
    install_requires=base_packages,
    extras_require={"dev": dev_packages},
    tests_require=test_packages,
    test_suite="tests",
    license_files=("LICENSE",),
    classifiers=[
        "Intended Audience :: Science/Research",
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
    ],
)
