# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.transmogrifier.transmogrifier import Transmogrifier


class ExampleImport(BrowserView):
    __call__ = ViewPageTemplateFile('example.pt')

    def exampleimport(self):
        transmogrifier = Transmogrifier(self.context)
        transmogrifier(u'exampleimport')
        return 'ok'



