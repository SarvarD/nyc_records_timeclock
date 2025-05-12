from setuptools import setup, find_packages

setup(
    name="timeclock",
    version="2.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "flask-sqlalchemy",
        "flask-migrate",
        "flask-bootstrap",
        "flask-kvsession",
        "flask-login",
    ],
)