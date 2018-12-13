from promebuilder import gen_metadata, setup
from promebuilder.utils import VERSIONFILE
from setuptools import find_packages
import os
import sys

if sys.version_info < (2, 5):
    sys.exit("requires python 2.5 and up")

here = os.path.dirname(__file__)
exec(open(os.path.join(here, 'rpyc', 'version.py')).read())
with open(os.path.join(here, VERSIONFILE), 'w') as verfile:
    verfile.write(locals().get('version_string'))

METADATA = gen_metadata(
    name="rpyc",
    description="Remote Python Call (RPyC), a transparent and symmetric RPC library",
    email="rpyc@googlegroups.com",
    url="http://rpyc.readthedocs.org",
    packages=[
        'rpyc',
        'rpyc.core',
        'rpyc.lib',
        'rpyc.experimental',
        'rpyc.utils',
    ],
    keywords="RPC",
    entry_points={
        'console_scripts': [
            "rpyc_classic = rpyc.scripts.rpyc_classic:main",
            "rpyc_registry = rpyc.scretips.rpyc_registry:main"
        ]
    }
)

# Disabling auto tests
for condatest in ['conda_import_tests', 'conda_command_tests']:
    if condatest in METADATA:
        METADATA[condatest] = False


METADATA.update(dict(
    author="Tomer Filiba",
    author_email="tomerfiliba@gmail.com",
    license="MIT",
    scripts=[
        os.path.join(here, "bin", "rpyc_classic.py"),
        os.path.join(here, "bin", "rpyc_registry.py"),
    ],
    tests_require=['nose'],
    test_suite='nose.collector',
    long_description=open(os.path.join(here, "README.rst"), "r").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Object Brokering",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Clustering",
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
    ],
))


if __name__ == '__main__':
    setup(METADATA)
