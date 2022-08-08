import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()


setuptools.setup(
    name='fizzbuzz2',
    version='2.1.14',
    description='Powerful Fizz Buzz Engine',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nbtk/fizzbuzz',
    author='nbtk',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
    ],
    packages=setuptools.find_packages(),
    install_requires=[],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'fizzbuzz=fizzbuzz.__main__:main',
        ],
    },
)
