Overview
=================

Django Knowledge is aiming to be a very simple knowledge base and question support engine, 
not entirely dissimilar to ZenKnowledge, Assistly, or HelpJuice, and to some degree 
StackOverflow or even UserVoice or GetSatisfaction.


.. _about-goals:

Goals of django-knowledge
--------------------

The goals of ``django-knowledge`` are simple and straightforward:

1. Searchable knowledge base.
2. A form to ask a missing question.
3. Staff can moderate via toolbar or Django's admin interface.


.. _about-how-it-works:

How django-knowledge works
---------------------

At its core, there are only a few moving parts, which keeps django-knowledge light and extensible.


Models
~~~~~~

There are only three data models in django-knowledge: **Question**, **Response** and **Category**. 
As you can imagine, **Question** is the base model which can have an arbitrary number or **Response**'s.
While **Response** is more or less a series of comments on a **Question**. **Question**'s can also
have an arbitrary number of **Categories**.

**Question**'s and **Response**'s can each be either *public*, *private* or *internal* (or 
*inheret* for **Response**). **Categories** are always *public*.


Views
~~~~~

In the same spirit, there are only 4 user facing views: **knowledge_index**, **knowledge_list**, 
**knowledge_thread**, and **knowledge_ask**.

- **knowledge_index** a general listing of popular questions plus search box
- **knowledge_list** listing of a specific subset of questions (by tags or search term)
- **knowledge_thread** response thread for a specific question
- **knowledge_moderate** a passthrough for moderators to manage questions & responses
- **knowledge_ask** form for asking a question


Templates
~~~~~~~~~

We provide default styles for the templates. You can easily embed this within your own shim/wrapper
or do nothing and just roll with the wrapper we provide. Read more in the :doc:`customize` section.


CSS (SASS)
~~~~~~~~~~~~~~~~~~

The included generic styles are compiled via SASS's scss. You can read more in the :doc:`customize` 
section. 
