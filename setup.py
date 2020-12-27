import setuptools


setuptools.setup(
    name='worklog',
    version='0.1',
    packages=setuptools.find_packages(),
    install_requires=['setuptools'],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'worklog=worklog.__main__:main',
            'wl=worklog.__main__:main' # or any specific function you would like
        ]
    },
)