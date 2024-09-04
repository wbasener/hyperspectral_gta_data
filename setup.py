from setuptools import setup

from hyperspectral_gta_data import __version_

setup(
    name='hyperspectral_gta_data',
    version=__version__,

    url='https://github.com/wbasener/hyperspectral_gta_data',
    author='Bill Basener',
    author_email='wb8by@virginia.edu',
    
    install_requires=[
        'gdown',
    ],
    
    py_modules=['hyperspectral_gta_data'],
)