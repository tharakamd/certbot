"""Example Certbot plugins.

For full examples, see `certbot.plugins`.

"""
import zope.interface
from acme import challenges

from certbot import interfaces
from certbot.plugins import common


@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(common.Plugin):
    """Example Authenticator."""

    description = "Example Authenticator plugin"

    def __init__(self, *args, **kwargs):
        super(Authenticator, self).__init__(*args, **kwargs)

    def prepare(self):
        pass

    def more_info(self):  # pylint: disable=missing-docstring,no-self-use
        return (
            'This plugin allows the user to customize setup for domain '
            'validation challenges either through shell scripts provided by '
            'the user or by performing the setup manually.')

    def get_chall_pref(self, domain):
        return [challenges.HTTP01]

    def perform(self, achalls):
        achall = achalls[0]
        response, validation = achall.response_and_validation()
        print validation
        return []

    def cleanup(self, achalls):
        print 'clean up'


# Implement all methods from IAuthenticator, remembering to add
# "self" as first argument, e.g. def prepare(self)...


@zope.interface.implementer(interfaces.IInstaller)
@zope.interface.provider(interfaces.IPluginFactory)
class Installer(common.Plugin):
    """Example Installer."""

    description = "Example Installer plugin"

    # Implement all methods from IInstaller, remembering to add
    # "self" as first argument, e.g. def get_all_names(self)...
