from setuptools import find_packages
from setuptools import setup


# Laden der Abhängigkeiten aus requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='fft_analysator',
    version='0.1.0',
    description='Ein FFT-Analysator für akustische Daten',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=required,  # Verwendung der geladenen Abhängigkeiten
    entry_points={
        'console_scripts': [
            # Konsolenskripte hier definieren, falls notwendig
        ]
    }
)
