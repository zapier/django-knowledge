Alerts
======

**django-knowledge** has built in functionality that sends email alerts to 
subscribed users when a new response is added or accepted. Users can opt-in 
or out this alert at the time of posting a question or response.

Further, Users with the flag 'is_staff' and the permission to change questions
will receive updates when a new question is added.

*TODO:* They can also opt-in or out after the fact.


Enabling
--------

By default, alerts are disabled. to enable them, simply add to your ``settings.py``:

.. code-block:: python
    
  KNOWLEDGE_ALERTS = True

Also ensure that the Django site framework is installed and setup properly, otherwise
the default links may not work properly.

.. code-block:: python
    
  SITE_ID = 1

  INSTALLED_APPS = (
      # ...
      'django.contrib.sites',
      # ...
  )


Scheduling
----------

By default, **django-knowledge** will greedily send emails via whatever email 
backend you have set during the request/response cycle. This is likely not 
desirable: we recommend using something like
`django-celery-email <https://bitbucket.org/schinckel/django-celery-email>`_ 
to delay the task via a queue. No further action is needed if you go this route. 

Alternatively, you can specify your own email function where you can introduce your
own off request functionality:

.. code-block:: python
    
    KNOWLEDGE_ALERTS_FUNCTION_PATH = 'path.to.your.own.function'

The email function should expect two keyword arguments:

* ``target_dict`` - A dictionary for {'me@dom.com': 'First Last (or username)'} for 
  anonymous or {'me@dom.com': <User instances>}. This list is deduplicated by email 
  address.
* ``response`` - A Response instance of the model triggering this alert. May be 
  ``None``. Only passed in when a new response is added.
* ``question`` - A Question instance of the model triggering this alert. May be 
  ``None``. Only passed in when a new question is added.
* ``**kwargs`` - It would be wise to include a blanket keyword arg catcher, we'll 
  likely add more things in the future, so this will keep your code from breaking.


**Note:** just to clarify: if you change the email function path setting, you will 
need to send the alert emails (or any other form of communication) yourself. Our 
builtin function will no longer act.


Templating
----------

We offer three default templates used to render both the subject and message of 
alert emails:

* ``django_knowledge/emails/subject.txt``
* ``django_knowledge/emails/message.txt``
* ``django_knowledge/emails/message.html``

Emails are sent with both txt and html formats. Simply override these if you want
to modify the defaults.