"""setup.py file."""
import uuid

from setuptools import setup, find_packages
from pip.req import parse_requirements

__author__ = 'Alcatel Lucent Enterprise <ebg_global_supportcenter@al-enterprise.com>'

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="napalm-aos",
    version="0.1.0",
    packages=find_packages(),
    author="Alcatel Lucent Enterprise",
    author_email="ebg_global_supportcenter@al-enterprise.com",
    zip_safe=False,
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/napalm-automation/napalm-aos",
    include_package_data=True,
    install_requires=reqs,
)
