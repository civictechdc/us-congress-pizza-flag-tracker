# Capitol Flag Pizza Tracker App

In collaboration with Modernization Staff Association.

Flask app proof of concept.

Frontend is available at https://github.com/codefordc/us-congress-pizza-flag-tracker-frontend

Live version is available at https://codefordc-flag.netlify.app/

See todos list: https://github.com/codefordc/us-congress-pizza-flag-tracker/blob/main/tasks.md

To run:
TODO: https://dev.to/mburszley/an-introduction-to-poetry-2b6n ?

# Local Deployment

## Conda Environment

If you have not created the conda environment for this project:

    ```
    conda create --name myenv
    ```
    

If the conda environment has been created:

    conda activate myenv
    pip install -r requirements.txt
    

## Python Environment without Conda
    
 If you have not created a Python environment for this project:

   python3 -m venv myenv
    

Then:
    
    source myenv/bin/activate
    
Choose:
    
    pip install -r requirements.txt --use-deprecated=legacy-resolver (faster)
     
        OR 
        
    pip install -r requirements.txt (takes a very long time - might be fixed in subsequent versions of pip)
    See https://stackoverflow.com/questions/65122957/resolving-new-pip-backtracking-runtime-issue for one article on the issue.
    

## Creating the database:

```
rm -rf migrations
rm flag*.db
DEBUG=True FLASK_APP=app.py flask db init
DEBUG=True FLASK_APP=app.py flask db migrate
DEBUG=True FLASK_APP=app.py flask db upgrade
```

After the database has been created:

    FLASK_APP=app.py FLASK_ENV=development flask run

## Security Configuration
All routes require log in except for create user, as this might get in the way of development.
Adding an order requires, create_update_delete_orders option must be set to Y.
To enable access to the routes, you can either: create an ADMIN account either with Add User option, 
log in to ADMIN without creating an account and specify any password (works only once) or (3) populating
with a script.  ADMIN options should have either ALL or Y specified.  At the time of this 
readme.md, only add user enforces the security authorization rules.

## Deploying to Heroku

```heroku create
heroku git:remote -a codefordc-flag
heroku config:set FLASK_APP=app.py FLASK_ENV=development
heroku run flask db init
heroku run flask db migrate
heroku run flask db upgrade
```
# Running tests

    pytest -s --verbose

# Viewing Data

`pip install datasette` first if needed
`datasette flag.db`


click the link (typically port 8001 on localhost)

or run `sqlite`


# TODOs:

- Plug some data in there along lines of the [Figma](https://www.figma.com/file/Lzq30lUA6N0hevjn8JVU6z/flag-requests)


# Ensemble Programming Environment

- https://mobti.me/flagpizza
- https://anydesk.com

# Security

## Resources used

To implement security, two tutorials were used: https://www.bacancytechnology.com/blog/flask-jwt-authentication and 
https://www.bezkoder.com/react-hooks-jwt-auth/.  Since the two tutorials were written separately, the flask app was tested 
with postman and then the react tutorial was modified to match up with what the flask was expecting.  This took some work
to do.

## User Security Options
Security is based on fields in users table:
- office_code - home office code.  Each office will have two accounts, one that can change passwords and one that can't.
For example, MA-01 and MA-01-ADMIN.  There will also be an account just called ADMIN with a home office of FED-ADMIN.
- can_crate_update_delete_orders: Y or N.  If Y, the user can create
orders and update and delete any orders.  This priv would be 
given to FED-ADMIN, FED-HOSS, and FED-XX offices.
- can_update_status_for: ALL, <office-code>, or NONE (might not need NONE).  If ALL, user can update any order.  
This would apply to all FED accounts and ADMIN.  <office-code> would be given to normal office accounts and admin accounts
(MA-01-ADMIN, MA-o1)
- can_update_password_for: ALL, <office_code>, SELF, NONE
- ALL would be given to ADMIN
- <office_code> would be given to admin for an office (for instance, office code of MA-01-ADMIN would be MA-01) and 
would allow that person to update their own password and the password for any user where office_code is MA-01.
- SELF would be given to office if you want an account to be able to change their own password.  Recommend only letting 
MA-01-ADMIN do that.
- NONE Could be given to office account (MA-01): choose between SELF and NONE

## Population
Here are how sample accounts should be populated:

ADMIN

Username ADMIN
office_code FED-ADMIN
can_update_status_for ALL
can_update_password_for NONE or SELF
can_create_update_delete_orders Y
is_admin Y

Username FED-HOSS / FED-AOC
office_code FED-HOSS / AOC-HOSS
can_update_status_for ALL
can_update_password_for NONE or SELF
can_create_update_delete__orders Y
is_admin N

FED-HOSS-ADMIN / AOC-HOS-ADMIN - same as above (including office code) except can_update_password_for 
would be FOS-HOSS or FED-AOC which would allow the admin to update password for FED-HOSS or FED-AOC

NJ-02
office_code NJ-o2
can_update_status_for NJ-02
can_update_password_for NONE or SELF
can_create_update_delete__orders N
is_admin N

NJ-02-ADMIN - same as above (including office code) except can_update_password_for 
would be FOS-HOSS or FED-AOC which would allow the admin to update password for NJ-02


office_code FED-HOSS / AOC-HOSS
can_update_status_for ALL
can_update_password_for NONE or SELF
can_create_update_delete__orders Y
is_admin N
 
# Guidelines
## Proposed
Backend
- When returning an error, use format  {"message": "<error message>", <error_number>).  For example, ???.  See ???.
- Use a parameter class for passing info
- Use table_record_to_json or table_to_json to convert from sqlalchemy to json in util.py
- Convert in the controller, not the actions
- If a function requires three or  more parameters, create a class to hold those params.  See UserParams
as an example.  This simplifies a bunch of code so you don't need to repeat.


## Accepted