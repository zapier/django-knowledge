Development
===========

Right now *django-knowledge* is still under heavy development. We're approaching the 
full development of this product in the manner described below.


.. _development-pattern:

Development pattern
-----------

1. **Documentation first!**
   
   This is vitally important as we pusposefully want to create something that 
   is a **best in class** application. We want django-knowledge be the premier
   help desk for django.

2. **Tests next!**
   
   Again, we want people to trust this application, so tests are an absolute must.
   TDD is the name of the game here. 100% coverage is the goal.

3. **Code final!**

   And let's make it good code as well. pep8 and all that jazz!


.. _development-guide:

Development guide
-----------------

Please join us in making django-knowledge the best open source help desk in the world!


Documentation
~~~~~~~~~~~~~

We're using **Sphinx**, so make sure you have ``pip install sphinx``, browse on into the
*docs* folder and run ``make html``:

.. code-block:: bash

   cd docs
   make html

Inside *docs/_build* should be the rendered html. Open up *docs/_build/html/index.html* in your 
browser to take a looksy.

Editing the files is equally simple, just adhere to the reStructuredText format. I recommend
using something like `watch <http://en.wikipedia.org/wiki/Watch_(Unix)>`_ while doing 
documentation to auto build everything while you work:

.. code-block:: bash

   cd docs
   watch make html


Tests
~~~~~

Inside the *tests* directory is a bash script that runs a localized Django project
that tests our application in a project context. A quick command should suffice for 
most basic needs:

.. code-block:: bash

   tests/runtests.sh

Right now we're not bundling tests inside the installed package, they are part of
their own example application. All tests are found in *tests/example/tests/* under split
out files reflecting their location in the package.

View the **coverage** stats by opening up the resulting *tests/reports/index.html*.


Code
~~~~

Setting up the **development server** is quite easy as well:

.. code-block:: bash

   pip install -r requirements.txt
   tests/syncdb.sh
   tests/runserver.sh

We do use `SASS <http://sass-lang.com/>`_ (and you should too!), so you will need to 
follow their install docs and then run something like:

.. code-block:: bash

   sass --watch knowledge/static/knowledge/scss:knowledge/static/knowledge/css

Please remember to run **pep8** and fix any errors you see, or explan why 
you won't in your commit message so we can yell at you:

.. code-block:: bash

   pep8 knowledge


Committing
~~~~~~~~~~

We work off of the **master branch** in our GitHub repo. Send a pull request! Tagged releases
will be pushed to PyPi.