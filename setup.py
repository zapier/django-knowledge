from distutils.core import setup

# Dynamically calculate the version based on mptt.VERSION
version_tuple = __import__('desk').VERSION
version = ".".join([str(v) for v in version_tuple])

setup(
    name = 'django-desk',
    description = '''A simple frontend and admin interface for dealing with help
        desk tickets and issues, including public and private responses and searching.''',
    version = version,
    author = 'Bryan Helmig',
    author_email = 'bryan@zapier.com',
    url = 'http://github.com/zapier/django-desk',
    packages=['desk'],
    package_data={'desk': ['templates/*']},
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)