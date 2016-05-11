from setuptools import setup

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'nose',
    'webtest',
    'pyramid-chameleon',
    'bs4',
    'lxml',
    'validators',
    'pep8',
    'flake8'
]

setup(name='wikipediafeed',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = wikipediafeed:main
      """,
)