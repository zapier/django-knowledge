Overview
=================

Django Desk is aiming to be a very simple knowledge base and question support engine, 
not entirely dissimilar to ZenDesk, Assistly, or HelpJuice, and to some degree 
StackOverflow or even UserVoice or GetSatisfaction.


.. _about-goals:

Goals of django-desk
--------------------

The goals of ``django-desk`` are simple and straightforward:

1. Searchable knowledge base.
2. A form to ask a missing question.
3. Staff can answer via Django's admin interface.


.. _about-how-it-works:

How django-desk works
---------------------

At its core, there are only a few moving parts, which keeps Django Desk light and extensible.


Models
~~~~~~

There are only two data models in Django Desk: **Question** and **Response**. As you can 
imagine, **Question** is the base model which can have an arbitrary number or **Response**'s.
While **Response** is more or less a series of comments on a **Question**.

**Question**'s and **Response**'s can each be either public or private (or inheret for **Response**).


Views
~~~~~

In the same spirit, there are only 3 user facing views: **question_index**, **question_list**, 
and **question_thread**. 

- **question_index** will have a general listing of of popular questions
- **question_list** will handle the listing of a specific subset of questions (like by categories or search term)
- **question_thread** will show the response thread