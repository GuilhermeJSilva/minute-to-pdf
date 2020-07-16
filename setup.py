from setuptools import setup

setup(name='quickPdf',
      version='0.1',
      description='',
      author='Guilherme Silva',
      license='MIT',
      packages=['minuteToPdf'],
      install_requires=[
          'graphviz',
      ],
      scripts=["scripts/quickPdf"])