"""
Minimal setup.py
Built using: https://github.com/ploomber/template
setup.py reference: https://setuptools.readthedocs.io/en/latest/setuptools.html
More on pkg structure: https://blog.ionelmc.ro/2014/05/25/python-packaging/
"""
import io
import re
import ast
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('src/mlspace/__init__.py', 'rb') as f:
    VERSION = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


with open("requirements.txt", "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='mlspace',
    version=VERSION,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    # package_data={"": ["*.txt", "*.rst", "*.sql", "*.ipynb"]},
    install_requires=[required_packages],
    extras_require={},
    entry_points={
        "console_scripts": [
            "mlspace = mlspace.main:app",
        ],
    },
)