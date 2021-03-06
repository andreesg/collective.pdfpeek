from setuptools import setup, find_packages


version = '1.2'

setup(name='collective.pdfpeek',
      version=version,
      description="A Plone 4 product that generates image thumbnail previews" +
      " of PDF files stored on ATFile based objects.",
      long_description=open("README.txt").read() + "\n" +
                       open("docs/INSTALL.txt").read() + "\n" +
                       open("docs/CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone Zope Python PDF',
      author='David Brenneman',
      author_email='db@davidbrenneman.com',
      url='https://github.com/dbrenneman/collective.pdfpeek',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pyPdf',
          'plone.app.registry',
          'plone.browserlayer',
          'plone.mocktestcase>=1.0b3',
          'Products.PloneTestCase',
          ],
      extras_require = {
          'test': [
              'Products.PloneTestCase',
              'plone.mocktestcase>=1.0b3',
              ]
          },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
