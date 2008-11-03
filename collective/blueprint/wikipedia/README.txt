==============================
collective.blueprint.wikipedia
==============================


    >>> from os.path import dirname, abspath
    >>> from collective.transmogrifier.tests import registerConfig
    >>> from collective.transmogrifier.transmogrifier import Transmogrifier
    >>> config = """
    ... [transmogrifier]
    ... pipeline =
    ...     source
    ...     printer
    ...     
    ... [source]
    ... blueprint = collective.blueprint.wikipedia
    ... xml = simplewiki-small-pages-articles.xml
    ...
    ... [printer]
    ... blueprint = collective.transmogrifier.pprinter
    ... """ 

    >>> registerConfig(u'test', config)
    >>> transmogrifier = Transmogrifier(plone)
    >>> transmogrifier(u'test')


