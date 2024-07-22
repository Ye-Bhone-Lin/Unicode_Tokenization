from setuptools import setup, find_packages

setup(
    name='unicode_tokenization',
    version='0.1',
    packages=find_packages(),
    install_requires=[
      re
    ],
    description='A Python library for syllable-based Unicode processing in Burmese.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ye Bhone Lin',
    author_email='yebhonelin10@gmail.com',
    url='https://github.com/Ye-Bhone-Lin/Unicode_Tokenization',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
