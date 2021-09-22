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

## Deploying to Heroku

```

heroku create
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
To implement security, two tutorials were used: https://www.bacancytechnology.com/blog/flask-jwt-authentication and 
https://www.bezkoder.com/react-hooks-jwt-auth/.  Since the two tutorials were written separately, the flask app was tested 
with postman and then the react tutorial was modified to match up with what the flask was expecting.  This took some work
to do.

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
 
