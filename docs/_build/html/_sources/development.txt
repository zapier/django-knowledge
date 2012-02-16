Development
===========

Right now *django-desk* is still under heavy development. We're approaching the 
full development of this product in the manner described below.


.. _development-pattern:

Development pattern
-----------

1. Documentation first!
   
   This is vitally important as we pusposefully want to create something that 
   is a **best in class** application. We want django-desk be the *south* of help
   desk software for Django. 

2. Tests next!
   
   Again, we want people to trust this application, so tests are an absolute must.
   TDD is the name of the game here. 100% coverage is the goal.

3. Code final!

   And let's make it good code as well. PEP8, pylint and all that jazz.


.. _development-guide:

Development guide
-----------------

Documentation
~~~~~~~~~~~~~

We're using Sphinx, so make sure you have ``pip install sphinx``, browse on into the
*docs* folder and run ``make html``. Inside *docs/_build* should be the rendered html.
Open up *docs/_build/html/index.html* in your browser to take a looksy.

Editing the files is equally simple, just adhere to the reStructuredText format. I recommend
using something like `watch <http://en.wikipedia.org/wiki/Watch_(Unix)>`_ and ``watch make html``
while doing doc works to auto build everything while you work.


Tests
~~~~~

Inside the *tests* directory is a bash script that runs a localized Django project
that tests our application in a project context. A quick command ``tests/runtests.sh``
should suffice.

Right now we're not bundling tests inside the installed package, they are part of
their own example application. 


Code
~~~~

Do your coding, but remember to run ``pep8 desk`` and pylint ``pylint desk`` and fix any
errors you see, or explan why you won't in your commit message.