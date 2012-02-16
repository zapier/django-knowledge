import os
# thanks https://github.com/tomchristie/django-rest-framework/blob/master/djangorestframework/tests/__init__.py

modules = [filename.rsplit('.', 1)[0]
           for filename in os.listdir(os.path.dirname(__file__))
           if filename.endswith('.py') and not filename.startswith('_')]
__test__ = dict()

for module in modules:
    exec("from example.tests.%s import __doc__ as module_doc" % module)
    exec("from example.tests.%s import *" % module)
    __test__[module] = module_doc or ""
