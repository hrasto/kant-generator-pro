import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kgp",
    version="0.0.2",
    author="Rastislav Hronsky",
    author_email="hronskyr@gmail.com",
    description="Python3 port of the Kant Generator Pro",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hrasto/kgp",
    project_urls={
        "Bug Tracker": "https://github.com/hrasto/kgp/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    package_data={
        "kgp": ["grammars/*.xml"],
    },
)