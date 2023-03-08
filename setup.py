from setuptools import setup

setup(
    name='hello-task',
    version='0.2',
    packages=['task_app'],
    description='task app',
    author='Roi Staff',
    author_email='roistaff1983@gmail.com',
    entry_points={
        'console_scripts': [
            'hello-task = task_app.task_app:autostart',
        ],
    },
)
