from setuptools import setup, find_packages

setup(
    name="dscamlib",
    version="0.1.0",
    description="Python library for interfacing with DSCam SDK",
    author="Lakruwan@noone",
    owner="antoniosegur141",
    packages=find_packages(),
    install_requires=[
        # List any Python dependencies here.
    ],
    # Include additional files into the package
    include_package_data=True
)
