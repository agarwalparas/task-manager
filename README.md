# How to Start

* Clone Repository
* Install Pip Requirements by creating a new virtual env of python 3.7
* Create a Postgres Db to save data
* Set OS Env Variables
    export FLASK_ENV=development/Production
    export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/<db_name>
    export JWT_SECRET_KEY=<secret-key>
* Run python run.py

# Supported API Calls

* Create User - POST api/v1/users
* Login User - POST api/v1/users/login
* Get A User Info - GET api/v1/users/<int:user_id>
* Get All users - GET api/v1/users
* Get My Info - GET api/v1/users/me
* Edit My Info - PUT api/v1/users/me
* DELETE My Account - DELETE api/v1/users/me
* Create Task - POST api/v1/tasks
* Get All Tasks - GET api/v1/tasks
* Get One Task - GET api/v1/tasks/<task_id>
* Update Task - PUT api/v1/tasks/<task_id>
* Delete Task - DELETE  api/v1/tasks/<task_id>
