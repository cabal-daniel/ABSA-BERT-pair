from setuptools import find_packages, setup

INSTALL_REQUIRES = [
    'click==8.0.3',
    'joblib==1.1.0',
    'nltk==3.6.5',
    'numpy==1.21.4',
    'pandas==1.3.5',
    'pkg_resources==0.0.0',
    'python-dateutil==2.8.2',
    'pytz==2021.3',
    'regex==2021.11.10',
    'scikit-learn==1.0.1',
    'scipy==1.7.3',
    'six==1.16.0',
    'sklearn==0.0',
    'threadpoolctl==3.0.0',
    'torch==1.10.1',
    'tqdm==4.62.3',
    'typing_extensions==4.0.1',
    'typer==0.4.0',
]

setup(
    name='cabal-absa',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
)
