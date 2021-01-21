
import setuptools
from setuptools import setup
setup(
    name='rt-thread-studio',
    version='2.1',
    description='Tools for RT-Thread Studio',
    author='RealThread',
    author_email='chenyaxing@rt-thread.com',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=setuptools.find_packages(),
    py_modules=['rt_thread_studio'],
    package_data={'rt_thread_studio': ['board_support_package_generator/template/temp.yaml','board_support_package_generator/template/debug/svd/*','board_support_package_generator/template/documents/images/*','board_support_package_generator/template/documents/manuals/*','board_support_package_generator/template/documents/sheet/*'],},
    include_package_data=True,
    install_requires=[
        'PyYAML>=5.3.1',
        'click>=7.1.1',
    ],
    entry_points='''
        [console_scripts]
        rt_tools=rt_thread_studio.rt_thread_studio_tools:cli
    ''',
)
