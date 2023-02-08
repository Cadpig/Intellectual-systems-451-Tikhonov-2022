from setuptools import setup

setup(
    name='pipelines',
    version='0.1.0',
    py_modules=['main_prefect'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'pipelines_prefect = main_prefect:api_flow',
        ],
    },
)
