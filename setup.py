from setuptools import setup, find_packages

setup(
    name='adventure_weave',
    version='1.0.0',
    url='https://github.com/adventure-weave/python_core.git',
    author='Michał Woźniczak',
    description='Simple commandline interpreter for Adventure Weave',
    packages=find_packages(),    
    install_requires=[
        'pyyaml',
    ],
    entry_points={
        'console_scripts': ['weave-story=adventure_weave.cli_player:main']
    },
)