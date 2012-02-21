Welcome to django-knowledge!
============================

django-knowledge makes it easy to add an integrated support desk, help desk or 
knowledge base to your Django project with only a few lines of boilerplate code.
While we give you a generic design for free, you should just as easily be able 
to customize the look and feel of the app if you like.

**django-knowledge** was developed internally for `Zapier <https://zapier.com/>`_.
Check out their `live demo <https://zapier.com/support/>`_.


At a glance:
------------

- Turn common questions or support requests into a **knowledge base**.
- Control **who sees what** with simple per object view permissions: *public* (everyone), 
  *private* (poster & staff), or *internal* (only staff).
- Assign questions and answers to **categories** for easy sorting.
- Staff get **moderation controls** or they can use the familiar *Django admin* to handle support requests.
- Allow **anonymous questions**, or require a standard Django user account (the default).
- Included base **templates and design** with prebundled HTML and CSS.
- BSD license.


Links:
------

* View a `live demo <https://zapier.com/support/>`_. This is the stock design, plus a 
  custom header and footer via an overridden base template.
* Check out the `documentation <http://django-knowledge.readthedocs.org/>`_ at ReadTheDocs.
* Visit our `GitHub repo <https://github.com/zapier/django-knowledge>`_ and join the development!


Screen Shots:
-------------

.. image:: https://github.com/zapier/django-knowledge/raw/master/docs/images/thread.png
   :width: 100 %
   :alt: a common thread viewed by anonymous user

.. image:: https://github.com/zapier/django-knowledge/raw/master/docs/images/thread-mod.png
   :width: 100 %
   :alt: a common thread viewed by a moderator (staff)

.. image:: https://github.com/zapier/django-knowledge/raw/master/docs/images/ask.png
   :width: 100 %
   :alt: ask form

.. image:: https://github.com/zapier/django-knowledge/raw/master/docs/images/home.png
   :width: 100 %
   :alt: the home page

.. image:: https://github.com/zapier/django-knowledge/raw/master/docs/images/results.png
   :width: 100 %
   :alt: search results with ask form at bottom

.. image:: https://github.com/zapier/django-knowledge/raw/master/docs/images/tests.png
   :alt: 100% coverage on tests
