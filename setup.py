from setuptools import setup, find_packages

version = '0.2'

setup(name='collective.blueprint.wikipedia',
      version=version,
      description="",
      long_description=open("README.rst").read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='zope plone transmogrifier blueprint wikipedia',
      author='Rok Garbas',
      author_email='rok@garbas.si',
      url='http://github.com/garbas/collective.blueprint.wikipedia',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.blueprint'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'lxml',
          'collective.transmogrifier',
          'plone.app.transmogrifier',
      ],
      )
