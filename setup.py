from setuptools import setup

__version__ = "0.1.2"

setup(
    name="Maisie-Sphinx-Theme",
    version=__version__,
    description="Sphinx theme used by Maisie.",
    long_description=open("README.rst").read(),
    author="Marek Kochanowski",
    author_email="marek@maisie.dev",
    url="https://github.com/maisie-dev/maisie-sphinx-theme",
    packages=["maisie_sphinx_theme"],
    include_package_data=True,
    install_requires=["Sphinx>1.3"],
    license="MIT",
    classifiers=(
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ),
)
