import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ftfutilities",
    version="1.0.1",
    author="Foxtrot Fanatics",
    author_email="foxtrotfanatics@gmail.com",
    description="Shared python utilities for Foxtrot Projects.",
    long_description="Shared python utilities for Foxtrot Projects.",
    long_description_content_type="text/markdown",
    url="https://github.com/FoxtrotCore/ftf-utilities",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)