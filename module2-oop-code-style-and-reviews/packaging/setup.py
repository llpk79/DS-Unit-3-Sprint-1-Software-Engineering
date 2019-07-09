import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='lambdata-pkutrich',
    version='0.0.4',
    author='Paul Kutrich',
    author_email='pkutrich@gmail.com',
    description='Some very basic DataFrame tools.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=
    'https://github.com/llpk79/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module2-oop-code-style-and-reviews',
    packages=setuptools.find_packages(),
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                 'Operating System :: OS Independent'],
)
