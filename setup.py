import setuptools

with open('README.md') as readme:
    long_desc = readme.read()

setuptools.setup(
    name='gistbin',
    version='0.1.2',
    author="Chandler Lofland (chand1012)",
    author_email='business@chand1012.net',
    description='Github Gist client allowing for quick uploads via commandline.',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url='https://github.com/chand1012/gistbin',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.24.0',
        'RandomWords>=0.3.0'
    ],
    scripts=['gistbin/gistbin']
)