from setuptools import setup, find_packages

setup(
    name="ml_pipeline",
    version="0.1",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch",
        "torchvision",
        "pytest",
    ],
) 