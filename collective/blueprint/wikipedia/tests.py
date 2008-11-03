
import unittest

from zope.testing import doctest
from zope.component import provideUtility

from plone.i18n.normalizer import urlnormalizer
from collective.transmogrifier.tests import setUp as baseSetUp
from collective.transmogrifier.tests import tearDown
from collective.transmogrifier.sections.tests import PrettyPrinter
from collective.transmogrifier.transmogrifier import Transmogrifier

from collective.blueprint.wikipedia.blueprint import Wikipedia


def setUp(test):
    baseSetUp(test)
        
    test.globs['transmogrifier'] = Transmogrifier(test.globs['plone'])

    provideUtility(urlnormalizer)
    provideUtility(Wikipedia, name=u'collective.blueprint.wikipedia')
    provideUtility(PrettyPrinter, name=u'collective.transmogrifier.pprinter')
    provideUtility(Wikipedia, name=u'collective.blueprint.wikipedia')

def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite('README.txt', setUp=setUp, tearDown=tearDown),
        ))

