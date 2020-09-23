
import setuptools
from setuptools import setup
setup(
    name='rt-thread-studio',
    version='1.1',
    description='Tools for RT-Thread Studio',
    author='RealThread',
    author_email='chenyaxing@rt-thread.com',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=setuptools.find_packages(),
    py_modules=['rt_thread_studio'],
    include_package_data=True,
    install_requires=[
        'PyYAML>=5.3.1'
    ],
)
