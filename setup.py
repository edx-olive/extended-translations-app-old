"""
Configuration file which sets up plugin and its settings to the edx-platform.
"""

from __future__ import absolute_import

import os
from setuptools import setup


def package_data(pkg, roots):
    """
    Find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.
    """

    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for file_name in files:
                data.append(os.path.relpath(os.path.join(dirname, file_name), pkg))

    return {pkg: data}


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='Extended Translations plugin for Open edX',
    version='0.0.1',
    description='Provides the way to extend and override translations for Open edX and it dependencies in one place',
    long_description=README,
    packages=['extended_translations'],
    requires=[],
    entry_points={
        "lms.djangoapp": ["extended_translations = extended_translations.apps:TranslationsPluginConfig"],
        "cms.djangoapp": ["extended_translations = extended_translations.apps:TranslationsPluginConfig"],
    }
)
