Introduction
============

Import blueprint is not yet done so please help import wikipedia to Plone_.

1. clone project::

    % git clone git://github.com/garbas/collective.blueprint.wikipedia.git

2. run buildout::

    % cd collective.blueprint.wikipedia
    % python boostrap.py
    % bin/buildout

3. run plone and create plone site with id Plone

4. download wikipedia articles and untar it::

    % wget http://dumps.wikimedia.org/simplewiki/latest/simplewiki-latest-pages-articles.xml.bz2
    % tar jxvf simplewiki-pages-articles-xml.bz2

4. make sure that you point to right xml in config::

    % vim simplewiki.cfg

4. run import::

   % bin/instance run import.py simplewiki.cfg Plone


TODO
----

 - Currently it fails around 20.000 items when trying to import ".htaccess"
 - recognize language wiki links (for now we are stripping them out)

.. _Plone: http://www.plone.org
