from setuptools import setup, find_packages

setup(
    name="motor-fault-detector",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn"
    ],
    author="Abdul Rafeul Mallick",
    description="Motor Fault Detection using SVM",
)
