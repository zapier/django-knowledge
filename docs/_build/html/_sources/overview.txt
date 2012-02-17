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
3. Staff can answer via Django's admin interface.


.. _about-how-it-works:

How django-knowledge works
---------------------

At its core, there are only a few moving parts, which keeps django-knowledge light and extensible.


Models
~~~~~~

There are only two data models in django-knowledge: **Question** and **Response**. As you can 
imagine, **Question** is the base model which can have an arbitrary number or **Response**'s.
While **Response** is more or less a series of comments on a **Question**.

**Question**'s and **Response**'s can each be either *public*, *private* or *internal* (or 
*inheret* for **Response**).


Views
~~~~~

In the same spirit, there are only 4 user facing views: **knowledge_index**, **knowledge_list**, 
**knowledge_thread**, and **knowledge_ask**.

- **knowledge_index** a general listing of of popular questions plus search box
- **knowledge_list** listing of a specific subset of questions (by tags or search term)
- **knowledge_thread** response thread for a specific question
- **knowledge_ask** form for asking a question


Templates
~~~~~~~~~

Templates are cool.


Javascript and CSS (CoffeeScript and SASS)
~~~~~~~~~~~~~~~~~~

We've included some generic styles and 
