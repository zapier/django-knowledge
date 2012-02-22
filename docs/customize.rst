Customize
=========

Since **django-knowledge** ships with default themes and styles, you might have
to spend a little time perfecting *your look*. However, it should work right out 
of the box with minimal setup (or none!) if you don't mind the defaults.

.. _customize-template:

Templates
---------

The default base template is ``django_knowledge/base.html`` which contains a 
single ``{% block knowledge_inner %}`` tag. This base template loads two css
files from your static (see below): ``reset.css`` and ``base.css``.

If you have your own template shim/wrapper:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Copy and modify ``django_knowledge/base.html`` to your own template folder. Edit
   it as you see fit.
2. Include ``{{ STATIC_URL }}knowledge/css/main.css`` for knowledge specific styling.
   You should purposefully leave out ``{{ STATIC_URL }}knowledge/css/reset.css`` if you 
   don't want us to reset your existing base styles.

If you do decide to change the base template via the ``KNOWLEDGE_BASE_TEMPLATE`` 
setting, your new template might look something like this:

.. code-block:: html
    
    <!doctype html>
    <html lang="en">
    <head>
      <title>{% block title %}{% endblock title %} | Johnny's Support Center</title>
      
      <link rel="stylesheet" href="{{ STATIC_URL }}css/my-own-reset.css">
      <link rel="stylesheet" href="{{ STATIC_URL }}css/my-own-style.css">

      <link rel="stylesheet" href="{{ STATIC_URL }}knowledge/css/main.css">
    </head>

    <body>
    <div class="wrapper">

      <div class="header">
          Welcome to the Johnny's app!
      </div>
      
      <div class="content">
        {% block knowledge_inner %}
          {% block content %}
            <!-- your tradition content is loaded here if not django knowledge -->
          {% endblock content %}

          <!-- django knowlege is loaded here -->
        {% endblock knowledge_inner %}
      </div>


      <div class="footer">
          Copyright 2012
      </div>
      
    </div>
    </body>
    </html>

That isn't to say that our css styles will fit in perfectly, but we've been careful 
to namespace under ``dk-``` the majority of our css classes, so conflicts should be
minimal.

If you want to use the included template shim/wrapper:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Ensure static resources are loading for ``{{ STATIC_URL }}knowledge/css/reset.css``
and ``{{ STATIC_URL }}knowledge/css/main.css``.
2. Done.


Modifying common singular sections:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two very common areas for modification:

1. ``django_knowledge/welcome.html`` - The support header containing the link and phrase 
   "Welcome to our Support Center". Simply override this locally by copying and editing 
   ``templates/django_knowledge/welcome.html`` to your project.

2. ``django_knowledge/sidebar.html`` - The sidebar containing links to the homepage, ask
   a question and categories. Likewise, simply override this locally by copying and editing 
   ``templates/django_knowledge/sidebar.html`` to your project.

3. ``django_knowledge/form.html`` - The form loops over given forms and renders them. 
   Likewise, you can simply override this locally by copying and editing 
   ``templates/django_knowledge/sidebar.html`` to your project.


.. _customize-static:

Static
------

As long as you are using Django's static files system, setting up static files should 
be as easy as ``python manage.py collectstatic``. If not, you can always copy your files
manually to a legacy ``MEDIA_URL`` and override the base template according to the above
templates section.

Likewise, feel free to override the included CSS with your own rules in your own stylesheets.
We'd recommend not editing the included CSS, as an update or ``collectstatic`` might
overwrite them.


.. _customize-css:

CSS
---

We purposefully namespace the majority of our css classes with ``dk-`` in order to keep 
them from conflicting with your existing css. There are two included css files:

* ``reset.css`` - The majority of the base classes that act on body, typography, etc... 
  This is ripped from Blueprint (though Blueprint is not a prerequisite). This should 
  probably only be included if you aren't using your own shim.
* ``main.css`` - This contains the real meat of the styles. Most of these are namespaced
  so they shouldn't affect your other styles (IE: the header/footer your shim has). 
  However, the inverse is not true. Your styles may (and probably will) effect knowledge's
  css. You're kind of on your own here.