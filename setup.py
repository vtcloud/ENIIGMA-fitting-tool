import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vtcloud", # Replace with your own username
    version="0.0",
    author="ENIIGMA Team",
    author_email="willrobsonastro@gmail.com",
    description="Spectral decomposition of IR ice spectrum",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vtcloud/ENIIGMA/tree/master",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "License :: Free for non-commercial use",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)