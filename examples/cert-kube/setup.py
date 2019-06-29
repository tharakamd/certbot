from setuptools import setup

setup(
    name='cert-kube',
    packages=['cert_kube'],
    include_package_data=True,
    version='1.0.2',
    install_requires=[
        'certbot',
        'zope.interface',
    ],
    entry_points={
        'certbot.plugins': [
            'kube_authenticator = cert_kube.kube:Authenticator'
        ],
    },
)
