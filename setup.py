import pathlib
import setuptools
from setuptools import setup
from setuptools import find_packages
# Current path.
here = pathlib.Path(__file__).parent.resolve()
# The long description of the "README".
long_description = (here / 'README.markdown').read_text(encoding='utf-8')
"""
Calling the setup function from setuptools
to install/build the package.
"""
setup(
    name='lander',
    version='1.0.0',
    description='*A small tool to compile static one-page pages from a template and some configuration files.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/iamtheblackunicorn/Lander',
    author='Alexander Abraham',
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=open('requirements.txt', 'r').read().split('\n'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'lander=lander:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/iamtheblackunicorn/Lander/issues',
        'Source': 'https://github.com/iamtheblackunicorn/Lander'
    },
)
