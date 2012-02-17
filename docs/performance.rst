Performance
===========

A few of the queries in the manager are a little crazy due to the need to 
check parent questions when responses are inherited status. We recommend
ensuring the following indexes for the following fields:

DB Indexes
----------

- **question & response `id`** (Django does by default)
- **question & response `user_id`** (Django does by default)
- **question & response `status`** (we do this by default because query by statuses a lot!)