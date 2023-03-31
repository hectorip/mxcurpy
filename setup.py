import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mxcurpy",
    version="0.0.1",
    author="Héctor Iván Patricio Moreno",
    author_email="hectorivanpatriciomoreno@gmail.com",
    description="Get the CURP and RFC for Mexican citizens",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="package URL",
    project_urls={
        "Bug Tracker": "package issues URL",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)
