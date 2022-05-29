from setuptools import setup, find_packages
with open("README.md", "r") as stream:
    long_description = stream.read()
setup(name="aminolib",version="1.1.1",author="@kingzero#6580",description="Library for Amino",long_description=long_description,install_requires=["datetime","flask","requests","json-minify"],keywords=["amino","aminolib","Lord","AminoAPI"],python_requires=">=3.6",url="https://github.com/pypa/sampleproject",project_urls={"aminolib": "https://github.com/pypa/sampleproject/issues",},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)