from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='arr',
    version='0.1',
    install_requires=requirements,
    packages=['arr',],
    license='Sonarr and Radarr API Wrapper'
)