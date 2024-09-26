from setuptools import setup, find_packages

setup(
    name='DivijEncrypt',
    version='0.1',
    author='Divij',
    author_email='divijchawla7@gmail.com',
    description='A Python library for various encryption methods, developed for educational purposes.',
    packages=find_packages(),
    install_requires=[
        'numpy',  # Add any other dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license="MIT",
)
