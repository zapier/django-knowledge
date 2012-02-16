Settings
========

Django Desk has its own series of custom settings you can use to tweak its operation.
As with normal Django settings, these go in ``settings.py``, or a variant thereof.


DESK_ALLOW_ANONYMOUS
--------------------

Default ``False``. If set to ``True``, users who are not logged in can ask questions. 
If ``False`` only registered and logged in users can ask questions.


DESK_AUTO_PUBLICIZE
-------------------

Default ``False``. If set to ``True``, answered questions are automatically published. 
If ``False``, staff must manually publish questions after answering.


DESK_FREE_RESPONSE
------------------

Default ``False``. If set to ``True``, any user (respecting DESK_ALLOW_ANONYMOUS)
can respond to any question. If ``False``, only staff or original poster may respond.


DESK_ALLOW_RATING
-----------------

Default ``True``. If set to ``True``, any user (respecting DESK_ALLOW_ANONYMOUS) can rate 
any response. If ``False``, ratings are disabled.