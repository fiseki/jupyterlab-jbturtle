from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

setup(
    name = 'jbturtle',
    version = '0.2.4',
    description = 'Simple turtle system for JupyterLab',
    install_requires = [
        'Pillow',
    ],
    packages = find_packages(),
    long_description = long_description,
    long_description_content_type = 'text/markdown'
)

