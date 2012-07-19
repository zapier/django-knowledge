Settings
========

Django Knowledge has its own series of custom settings you can use to tweak its 
operation. As with normal Django settings, these go in ``settings.py``, or a variant 
thereof.


KNOWLEDGE_ALLOW_ANONYMOUS
-------------------------

Default ``False``. If ``True``, users who are not logged in can ask questions. If 
``False`` only registered and logged in users can ask questions.


KNOWLEDGE_LOGIN_REQUIRED
------------------------

Default ``False``. If ``True`` users that are not authenticated are redirected to
LOGIN_URL.


KNOWLEDGE_AUTO_PUBLICIZE
------------------------

Default ``False``. If ``True``, answered questions are automatically published. If 
``False``, staff must manually publish questions after answering.


KNOWLEDGE_FREE_RESPONSE
-----------------------

Default ``True``. If ``True``, any user (respecting KNOWLEDGE_ALLOW_ANONYMOUS) can 
respond to any question. If ``False``, only staff or original poster may respond.


KNOWLEDGE_SLUG_URLS
-------------------

Default ``True``. If ``True``, the URL for a question will have the slug from its
title appended to the end and incorrect or missing slugs will result in a 301 redirect. 
If ``False``, the slug is ommitted.


KNOWLEDGE_ALERTS
----------------

Default ``False``. If ``True``, we'll send a signal to the function defined in 
``KNOWLEDGE_ALERTS_FUNCTION_PATH`` and outlined in :doc:`alerts`. If ``False`` we
will not.


KNOWLEDGE_ALERTS_FUNCTION_PATH
------------------------------

Default ``knowledge.signals.send_alerts``. This should be the path to a function 
as defined in :doc:`alerts`. Depends on ``KNOWLEDGE_ALERTS`` to be active.