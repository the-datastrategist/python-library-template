from setuptools import setup, find_packages

setup(
    name='python_libray_template',
    version='0.1.0',
    author='Gordon Silvera',
    description='A template for Python libraries that support data science projects',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.5',
        'numpy>=1.22',
        'scikit-learn>=1.2',
    ],
)
