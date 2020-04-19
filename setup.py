from setuptools import find_packages, setup

setup(
    name='cmbdb',
    description='Database of basic properties of CMB experiments',
    author='Davide Poletti',
    author_email='davide.pole@gmail.com',
    url='https://github.com/dpole/cmbdb',
    license='GPLv3',
    install=['cmbdb'],
    packages=find_packages(),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=['pandas', 'pyaml'],
)
