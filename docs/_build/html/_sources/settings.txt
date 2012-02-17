Settings
========

Django Desk has its own series of custom settings you can use to tweak its operation.
As with normal Django settings, these go in ``settings.py``, or a variant thereof.


DESK_ALLOW_ANONYMOUS
--------------------

Default ``False``. If ``True``, users who are not logged in can ask questions. 
If ``False`` only registered and logged in users can ask questions.


DESK_AUTO_PUBLICIZE
-------------------

Default ``False``. If ``True``, answered questions are automatically published. 
If ``False``, staff must manually publish questions after answering.


DESK_FREE_RESPONSE
------------------

Default ``False``. If ``True``, any user (respecting DESK_ALLOW_ANONYMOUS) can 
respond to any question. If ``False``, only staff or original poster may respond.


DESK_ALLOW_RATING
-----------------

Default ``True``. If ``True``, any user (respecting DESK_ALLOW_ANONYMOUS) can 
rate any response. If ``False``, ratings are disabled.


DESK_SLUG_URLS
--------------

Default ``True``. If ``True``, the URL for a question will have the slug from its
title appended to the end and incorrect or missing slugs will result in a 301 redirect. 
If ``False``, the slug is ommitted.


DESK_LOAD_JQUERY
----------------

Default ``True``. If ``True``, we'll load our local static jQuery. If ``False``, we don't
and you will need to.