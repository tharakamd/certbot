from setuptools import setup


setup(
    name='kube',
    package='certbot_example_plugins.py',
    install_requires=[
        'certbot',
        'zope.interface',
    ],
    entry_points={
        'certbot.plugins': [
            'kube_authenticator = certbot_example_plugins:Authenticator'
        ],
    },
)
