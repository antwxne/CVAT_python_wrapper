import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CVAT wrapper",
    version="1.0.0",
    author="antwxne",
    author_email="antoine.desruet@epitech.eu",
    description="Python wrapper for CVAT API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antwxne/CVAT_python_wrapper",
    project_urls={
        "Bug Tracker": "https://github.com/antwxne/CVAT_python_wrapper/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)