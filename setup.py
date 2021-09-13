"""Rangeon package setup."""

import os

from setuptools import find_namespace_packages, setup

REQUIREMENTS = {
    'common': [
        'tqdm==4.62.2',
    ],
    'maps': [
        'plotly',
        'matplotlib==3.3.4',
        'perlin-noise==1.7',
        'numpy==1.21.2',
    ],
    'development': [
        'astroid>=2.6.6',
        'pep8>=1.7.1',
        'pycodestyle>=2.7.0',
        'pylint>=2.9.6',
    ]
}

# Dictionary of resources to add to the package.
# - key: package that will provide the given file
# - values: list of paths of the files to add starting from git root
RESOURCES = {
}

# - Commands
CONSOLE_SCRIPTS = [
    'rangeon-gen-maps=rangeon.maps:generate',
]

setup(
    name='rangeon',
    packages=find_namespace_packages(exclude=[]),
    version='0.0.1',
    author='Lorenzo Andraghetti',
    author_email='andraghetti.l@gmail.com',
    maintainer_email='andraghetti.l@gmail.com',
    license='MIT',
    url='https://github.com/andraghetti/rangeon',
    download_url='https://github.com/andraghetti/rangeon',
    platforms=['any'],
    install_requires=REQUIREMENTS['common'] + REQUIREMENTS['maps'],
    extras_require={'dev': REQUIREMENTS['development']},
    python_requires='~=3.9.7',
    package_data={
        package: [os.path.basename(file_path) for file_path in files]
        for package, files in RESOURCES.items()
    },
    include_package_data=True,
    zip_safe=True,
    entry_points={'console_scripts': CONSOLE_SCRIPTS},
)
