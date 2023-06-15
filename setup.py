import pathlib

from setuptools import setup

setup(
    name="ruaj-testpypi",
    description="Testing PyPi",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://equinor.com",
    use_scm_version={"write_to": "src/ruaj/testpypi/version.py"},
    author="ruaj",
    license="MIT",
    keywords="pypi",
    classifiers=[
        "Programming Language :: Python :: 3.10"
    ],
    author_email="myemail@something.com",
    entry_points={},
    install_requires=[],
    setup_requires=["setuptools_scm~=3.2"],
    python_requires="~=3.10"
)
