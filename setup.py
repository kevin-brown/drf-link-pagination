from setuptools import setup, find_packages
from rest_link_pagination import __version__
import os


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(
    name="drf-link-pagination",
    version=__version__,
    url="https://github.com/kevin-brown/drf-link-pagination",
    license="MIT",
    description="Add `Link`-based pagination to your API.",
    author="Kevin Brown",
    author_email="kbrown@rediker.com",
    packages=find_packages(exclude=["tests*", ]),
    package_data=get_package_data("rest_link_pagination"),
    install_requires=[
        "Django>=1.6",
        "djangorestframework>=2.3"
    ]
)
