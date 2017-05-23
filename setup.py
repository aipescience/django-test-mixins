from setuptools import setup, find_packages

version = '0.1.2'

setup(
    name='django-client-test-mixins',
    packages=find_packages(),
    license=u'Apache License (2.0)',
    version=version,
    description='A set of mixins to automatically generate test for generic Django views and DRF Viewsets.',
    author='Jochen Klar',
    author_email='jklar@aip.de',
    maintainer=u'AIP E-Science',
    maintainer_email=u'escience@aip.de',
    url='https://github.com/aipescience/django-client-test-mixins',
    download_url='https://github.com/aipescience/django-client-test-mixins/archive/%s.tar.gz' % version,
    keywords=['testing', 'django'],
    classifiers=[],
)