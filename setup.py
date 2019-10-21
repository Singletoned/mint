from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='mint',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'PasteDeploy==1.3.2',
          'Paste==1.7.2',
          'PasteScript==1.7.3',
          'Elixir==0.6.1',
          'SQLAlchemy==0.5.0',
          'WerkZeug==0.15.3',
          'FormEncode==1.2.1',
          'Beaker==1.1.3',
          'WebTest==1.1',
          'nose==0.10.4',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.app_factory]
      main = mint.wsgiapp:make_app
      """,
      )
