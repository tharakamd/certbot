"""Example Certbot plugins.

For full examples, see `certbot.plugins`.

"""
import zope.interface

from certbot import interfaces
from certbot.plugins import common


@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(common.Plugin):
    """Example Authenticator."""

    description = "Example Authenticator plugin"

    def get_chall_pref(self, domain):  # pragma: no cover
        # pylint: disable=missing-docstring,no-self-use,unused-argument
        return []

    def perform(self, achalls):  # pylint: disable=missing-docstring
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
