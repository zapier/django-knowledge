from distutils.core import setup

# Dynamically calculate the version based on mptt.VERSION
version_tuple = __import__('knowledge').VERSION
version = '.'.join([str(v) for v in version_tuple])

setup(
    name = 'django-knowledge',
    description = '''A simple frontend and admin interface for dealing with help
        knowledge tickets and issues, including public and private responses and searching.''',
    version = version,
    author = 'Bryan Helmig',
    author_email = 'bryan@zapier.com',
    url = 'http://github.com/zapier/django-knowledge',
    install_requires=['Markdown>=2.1.1',],
    packages=['knowledge'],
    package_data={'knowledge': [
      'migrations/*.py',
      'static/knowledge/css/*.css',
      'templates/django_knowledge/*.html',
      'templates/django_knowledge/emails/*.html',
      'templatetags/*.py']},
    classifiers = ['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)