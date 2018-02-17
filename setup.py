#!/usr/bin/python3

from setuptools import setup, find_packages

def generate_data_files(prefix, directories):
    import os

    data_files = []
    for dir in directories:
        for root, dirs, files in os.walk(dir):
            local_files = []
            for file in files:
                local_files.append(os.path.join(root, file))
            if local_files:
                data_files.append((prefix + '/' + root, local_files))
    return data_files


setup(
    name='bot',
    version=0.1,
    description='A powerful bot for a discord server',
    long_description=('A powerful bot for a discord server'),
    author='Matthieu SISCA',
    author_email='matthieu.sisca@gmail.com',
    packages=find_packages(),
    install_requires=[
        'discord',
        'argparse',
    ],

    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    # package_data={'scripts': ['templates/*']},
    # data_files=generate_data_files('www/website', ['app', 'static']),

    # test_suite="tests",

    entry_points={
        'console_scripts': [
            'insult_bot=bot.main:main',
        ],
    },
)
