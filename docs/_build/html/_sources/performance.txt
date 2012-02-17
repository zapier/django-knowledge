Performance
===========

A few of the queries in the manager are a little crazy due to the need to 
check parent questions when responses are inherited status. We recommend
ensuring the following indexes for the following fields:

DB Indexes
--------------------

- **question.id** (Django does by default)
- **question.user_id** (Django does by default)
- **question.status** (we query by statuses a lot!)
- **response.id** (Django does by default)
- **response.user_id** (Django does by default)
- **response.status** (we query by statuses a lot!)