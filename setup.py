from ftf_utilities import VERSION
import ftf_utilities, setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ftf_utilities",
    version=VERSION,
    author="Foxtrot Fanatics",
    author_email="foxtrotfanatics@gmail.com",
    packages=['ftf_utilities'],
    scripts=[],
    url="https://github.com/FoxtrotCore/ftf-utilities",
    license="MIT",
    description="Shared python utilities for Foxtrot Projects.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.0',
)
