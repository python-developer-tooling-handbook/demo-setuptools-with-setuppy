from setuptools import setup, find_packages

setup(
    name="setuptools-with-setuppy",
    version="0.2",
    description="This is a demo package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="",  # Add the author's name if available
    author_email="",  # Add the author's email if available
    license="Apache-2.0",
    url="",  # Add the URL of the project if available
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "cowsay",
    ],
    extras_require={
        "test": ["pytest"],
    },
)
