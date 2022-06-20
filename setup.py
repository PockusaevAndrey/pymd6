from setuptools import setup, find_packages

setup(
    name='pymd6',
    packages=find_packages(),
    version='0.1.1',
    description='Simple library to calculate MD6 checksum',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Pokusaev Andrey",
    license="MIT",
    author_email='pockusaevandrey@yandex.ru',
    url='https://github.com/PockusaevAndrey/pymd6',
    keywords=['MD6'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
