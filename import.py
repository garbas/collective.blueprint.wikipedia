
import os
import argparse
import transaction

from AccessControl.User import UnrestrictedUser
from AccessControl.SecurityManagement import newSecurityManager

from collective.transmogrifier.transmogrifier import Transmogrifier
from collective.transmogrifier.transmogrifier import configuration_registry


if __name__ == '__main__':
    """
    Example:
        % ./bin/instance run import.py some_transmogrifier_configuration.cfg Plone
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('cfg')
    parser.add_argument('site')
    args_ = parser.parse_args()

    filepath = os.path.abspath(args_.cfg)
    filename = os.path.basename(filepath)
    configuration_registry.registerConfiguration(
                filename, filename, filepath, filepath)

    admin = UnrestrictedUser('admin', '', ['Manager'], '')
    newSecurityManager(None, admin)

    site = app[args_.site]

    Transmogrifier._raw = []  # TODO: bad bad boy, put this upstream
    Transmogrifier(site)(filename)

    transaction.commit()


