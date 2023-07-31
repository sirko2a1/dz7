from setuptools import setup

setup(
    name='clean_folder', 
    version='0.1', 
    description='A Python package to sort files in a folder', 
    author='I am',  
    install_requires=[], 
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean_folder.clean:main' #(модуль.підмодуль.функція:функція-запуску)
        ]
    }
)
