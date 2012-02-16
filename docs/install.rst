Install
=======

 - :ref:`Using pip or easy_install <installation-pip>`, which is most common for stable releases.
 - :ref:`Using a Git checkout <installation-git>`, recommended if you want cutting-edge features.
 - :ref:`Using downloadable archives <installation-archives>`, useful if you don't have pip or git.


.. _installation-pip:
 
Using pip or easy_install
-------------------------

We highly recommend using pip to install *django-desk*, the packages are regularly updated 
with stable releases:

.. code-block:: bash

   pip install django-desk

Or, alternatively:

.. code-block:: bash

   easy_install django-desk

But really, you shouldn't do that.


.. _installation-git:
 
Using git repositories
----------------------

Regular development happens at our`github repo <https://github.com/zapier/django-desk>`_. Grabbing the 
cutting edge version might give you some extra features or fix some newly discovered bugs. We recommend
not installing from the git repo unless you are actively developing *django-desk*. Please don't
use it in production (and if you do, report back what broked)!

.. code-block:: bash

   git clone git@github.com:zapier/django-desk.git django-desk

You can add the **desk** folder inside the resulting **django-desk** to your PYTHONPATH or 
simply run ``python setup.py install`` to add it to your **site-packages**.


.. _installation-archives:
 
Using archives (tarball or zip)
------------------------------

Visit our `tags page <https://github.com/zapier/django-desk/tags>`_ to grab the archives of 
both current and previous stable releases. After unzipping or untarring, you can add the **desk** 
folder inside the resulting **django-desk** to your PYTHONPATH or simply run ``python setup.py install`` 
to add it to your **site-packages**.
