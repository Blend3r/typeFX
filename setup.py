from setuptools import setup, find_packages

setup(
    name='typeFX',
    version='0.1.0',
    description='A package with a typing effect and sound',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'typeFX': ['typeFX/sounds/spacebar-click-keyboard-199448-[AudioTrimmer.com].mp3'],  # Include sound files in the package
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
