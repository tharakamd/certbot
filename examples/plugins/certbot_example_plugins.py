"""Example Certbot plugins.

For full examples, see `certbot.plugins`.

"""
import requests
import zope.component
import zope.interface
from acme import challenges

from certbot import interfaces
from certbot import reverter
from certbot.plugins import common


@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(common.Plugin):
    _HTTP_INSTRUCTIONS = """\
    Create a file containing just this data:

    {validation}

    And make it available on your web server at this URL:

    {uri}
    
    And 
    {encoded_token}
    """

    description = "Example Authenticator plugin"

    def __init__(self, *args, **kwargs):
        super(Authenticator, self).__init__(*args, **kwargs)
        self.reverter = reverter.Reverter(self.config)
        self.reverter.recovery_routine()
        self.env = dict() \
            # type: Dict[achallenges.KeyAuthorizationAnnotatedChallenge, Dict[str, str]]
        self.subsequent_dns_challenge = False
        self.subsequent_any_challenge = False

    def prepare(self):
        print "### plugin preparation done ###"

    def more_info(self):  # pylint: disable=missing-docstring,no-self-use
        return (
            'This plugin can be used to authenticate custom domain '
        )

    def get_chall_pref(self, domain):
        return [challenges.HTTP01]

    def perform(self, achalls):
        achall = achalls[0]
        validation = achall.validation(achall.account_key)
        msg = self._HTTP_INSTRUCTIONS.format(achall=achall, encoded_token=achall.chall.encode('token'),
                                             port=self.config.http01_port, uri=achall.chall.uri(achall.domain),
                                             validation=validation)

        display = zope.component.getUtility(interfaces.IDisplay)
        self._create_challenge_content(achall.chall.encode('token'), validation, display)
        display.notification(msg, pause=False, wrap=False, force_interactive=True)
        self.subsequent_any_challenge = True

        return [achall.response(achall.account_key)]

    def _create_challenge_content(self, challenge_id, challenge_content, display):
        URL = "http://172.30.14.130:30050/challenges"
        data = {
            "challenge_content": challenge_content,
            "challenge_id": challenge_id
        }
        r = requests.post(url=URL, data=data)
        display.notification(r.json(), pause=False, wrap=False, force_interactive=True)

    def cleanup(self, achalls):
        print "### cleaning challenges"
        self.reverter.recovery_routine()


# Implement all methods from IAuthenticator, remembering to add
# "self" as first argument, e.g. def prepare(self)...


@zope.interface.implementer(interfaces.IInstaller)
@zope.interface.provider(interfaces.IPluginFactory)
class Installer(common.Plugin):
    """Example Installer."""

    description = "Example Installer plugin"

    # Implement all methods from IInstaller, remembering to add
    # "self" as first argument, e.g. def get_all_names(self)...
