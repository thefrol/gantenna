from setuptools import setup, find_packages
from pathlib import Path
here=Path(__file__).parent

setup(
     name='gantenna',
     version='0.0.1',
     description='VQGAN+RUCLIP image sythesis',
     package_dir={'': 'src'},
     packages=find_packages(where='src'),
     install_requires=open('requirements.txt').readlines(),
 )
