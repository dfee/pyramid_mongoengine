import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid', # wsgiref server entry point
    'pyramid-beaker',
    'pyramid-debugtoolbar',
    'pyramid-exclog',
    'pyramid-jinja2',
    'mongoengine',
    'py-bcrypt',
    'waitress',
    'deform',]

setup(name='pyramid_mongoengine',
      version='0.1',
      description='MongoEngine bindings for the Pyramid web framework',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Framework :: Pylons",
        "License :: Repoze Public License",
        ],
      author='Devin Fee',
      author_email="pylons-discuss@googlegroups.com",
      url='',
      keywords='web wsgi pyramid pylons mongoengine',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pyramid_mongoengine",
      entry_points = """\
        [paste.paster_create_template]
        pyramid_mongoengine=pyramid_mongoengine.scaffolds:MongoEngineProjectTemplate
        [pyramid.scaffold]
        pyramid_mongoengine=pyramid_mongoengine.scaffolds:MongoEngineProjectTemplate
      """,
      )

