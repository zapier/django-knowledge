Install
=======

 - :ref:`Using pip or easy_install <installation-pip>`, which is most common for stable releases.
 - :ref:`Using a Git checkout <installation-git>`, recommended if you want cutting-edge features.
 - :ref:`Using downloadable archives <installation-archives>`, useful if you don't have pip or git.


.. _installation-pip:
 
Using pip or easy_install
-------------------------

We highly recommend using pip to install *django-knowledge*, the packages are regularly updated 
with stable releases:

.. code-block:: bash

   pip install django-knowledge

Or, alternatively:

.. code-block:: bash

   easy_install django-knowledge

But really, you shouldn't do that.


.. _installation-git:
 
Using git repositories
----------------------

Regular development happens at our `GitHub repository <https://github.com/zapier/django-knowledge>`_. Grabbing the 
cutting edge version might give you some extra features or fix some newly discovered bugs. We recommend
not installing from the git repo unless you are actively developing *django-knowledge*. Please don't
use it in production (and if you do, report back what broked)!

.. code-block:: bash

   git clone git@github.com:zapier/django-knowledge.git django-knowledge

You can add the **knowledge** folder inside the resulting **django-knowledge** to your PYTHONPATH or 
simply run ``python setup.py install`` to add it to your **site-packages**.


.. _installation-archives:
 
Using archives (tarball or zip)
------------------------------

Visit our `tags page <https://github.com/zapier/django-knowledge/tags>`_ to grab the archives of 
both current and previous stable releases. After unzipping or untarring, you can add the **knowledge** 
folder inside the resulting **django-knowledge** to your PYTHONPATH or simply run ``python setup.py install`` 
to add it to your **site-packages**.



.. _installation-setup:
 
Setting up your Django project
------------------------------

First, you'll want to add ``knowledge`` and ``django.contrib.markup`` to your ``INSTALLED_APPS``. You may 
need to ``pip install markdown`` to cover the markup dependency.

..  code-block:: python

    INSTALLED_APPS = (
        'django.contrib.contenttypes',
        'django.contrib.comments',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.admin',

        # Your favorite apps

        'django.contrib.markup',
        'knowledge',)


Second, add ``url(r'^knowledge/', include('knowledge.urls'))`` to your ``urls.py``.

..  code-block:: python

    
    urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),

        # your url patterns

        url(r'^knowledge/', include('knowledge.urls')),
    )


Third, be sure to run ``python manage.py syncdb`` or ``python manage.py migrate knowledge`` to set up
the necessary database tables.

.. code-block:: bash

   python manage.py syncdb
   # or...
   python manage.py migrate knowledge


Finally, follow the steps outlined in the :doc:`customize` section for templates and static resources.
Short version, don't forget to run ``python manage.py collectstatic``.

.. code-block:: bash

   python manage.py collectstatic