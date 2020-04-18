from distutils.core import setup

setup(
    name='cmbdb',
    version='1.0',
    description='Database of basic properties of CMB experiments',
    author='Davide Poletti',
    author_email='davide.pole@gmail.com',
    url='https://github.com/dpole/cmbdb',
    license='GPLv3',
    install=['cmbdb'],
    packages=['cmbdb'],
    include_package_data=True,
    setup_requires=['setuptools-git'],
    install_requires=['pandas', 'pyaml'],
)
