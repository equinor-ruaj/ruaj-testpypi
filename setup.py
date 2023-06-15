from setuptools import setup

setup(
    name="ruaj-testpypi",
    description="Testing PyPi",
    url="myurl",
    use_scm_version={"write_to": "src/ruaj/testpypi/version.py"},
    author="ruaj",
    license="MIT",
    keywords="pypi",
    classifiers=[
        "Programming Language :: Python :: 3.10"
    ],
    author_email="myemail",
    entry_points={},
    install_requires=[],
    setup_requires=["setuptools_scm~=3.2"],
    python_requires="3.10"
    
)