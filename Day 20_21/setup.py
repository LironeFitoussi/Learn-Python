from setuptools import setup

APP = ["main.py"]
OPTIONS = {
    "argv_emulation": True,
    "packages": ["turtule", "random"],  # Add required packages here
}

setup(
    app=APP,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
