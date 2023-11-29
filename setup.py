from setuptools import setup, find_packages


def get_version():
    return '0.1.0'


def get_requirements():
    with open('requirements.txt', 'r') as file:
        return file.read()


VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='merman_wrapper',
    version=VERSION,
    description='Runs merman using wasmtime',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Luka Mate Granic',
    author_email='luka.granic@microblink.com',
    url='https://github.com/microblink/merman-pip-wrapper',
    license='MIT',
    packages=find_packages(),
    package_data={'merman_wrapper': ['wasm_files/merman.wasm']},
    install_requires=get_requirements(),
    include_package_data=True,
    entry_points="""
        [console_scripts]
        merman_wrapper = merman_wrapper.main:main
    """,
    data_files=['requirements.txt'],

)
