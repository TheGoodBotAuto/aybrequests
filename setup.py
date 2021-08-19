from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='AYBRequests',
    url='https://github.com/jladan/package_demo',
    author='Joshua Tower',
    author_email='joshua.tower@gmail.com',
    # Needed to actually package something
    packages=['aybrequests'],
    # Needed for dependencies
    install_requires=[],
    # *strongly* suggested for sharing
    version='0.1.0',
    # The license can be anything you like
    license='MIT',
    description='Wrapper for requests package that includes base settings such as base url',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)