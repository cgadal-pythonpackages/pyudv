from setuptools import setup, find_packages

setup(
    name="pyudv",
    version="0.1",
    url="https://github.com/cgadal/pyudv",
    author="Cyril Gadal",
    author_email="cyril.gadal@imft.fr",
    license="GNU",
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3",
    install_requires=["numpy", "matplotlib", "datetime", "scipy"],
)
