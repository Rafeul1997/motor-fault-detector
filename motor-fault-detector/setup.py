from setuptools import setup, find_packages

setup(
    name="motor-fault-detector",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn"
    ],
    author="Your Name",
    description="Motor Fault Detection using SVM",
)
