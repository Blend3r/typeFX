from setuptools import setup, find_packages

setup(
    name='typeFX',  # The name of your package
    version='0.1.0',  # The version of your package
    description='A package with a typing effect and sound',  # Short description
    author='Diego Escalante',  # Add your name or your organization's name
    author_email='3dpr1nt3rb0y@gmail.com',  # Add your email for contact
    url='https://github.com/Blend3r/typeFX',  # URL to your GitHub repository
    packages=find_packages(),  # Automatically find packages in your project
    include_package_data=True,  # Include non-Python files specified in package_data
    package_data={
        'typeFX': ['sounds/spacebar-click-keyboard-199448-[AudioTrimmer.com].mp3'],  # Make sure this path is correct
    },
    classifiers=[
        'Programming Language :: Python :: 3',  # Python version
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',  # OS compatibility
    ],
    python_requires='>=3.13',  # Minimum required Python version
)
