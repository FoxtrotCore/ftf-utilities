import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ftfutils",
    version="2.0.1",
    author="Foxtrot Fanatics",
    author_email="foxtrotfanatics@gmail.com",
    packages=['ftfutils'],
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
