# Capitol Flag Pizza Tracker App

In collaboration with Modernization Staff Association.

Flask app proof of concept.

Frontend is available at https://github.com/codefordc/us-congress-pizza-flag-tracker-frontend

Live version is available at https://codefordc-flag.netlify.app/

See todos list: https://github.com/codefordc/us-congress-pizza-flag-tracker/blob/main/tasks.md

To run:
TODO: https://dev.to/mburszley/an-introduction-to-poetry-2b6n ?

# Local Deployment

If using conda:

    conda create --name myenv
    

Then:

    conda activate myenv
    pip install -r requirements.txt
    

**OR if using python, set up your Python environment:**
    
    python3 -m venv myenv
    

Then:
    
    source myenv/bin/activate
    pip install -r requirements.txt
    

To create the database:

```
rm -rf migrations
rm flag*.db
DEBUG=True FLASK_APP=app.py flask db init
DEBUG=True FLASK_APP=app.py flask db migrate
DEBUG=True FLASK_APP=app.py flask db upgrade
DEBUG=True FLASK_APP=app.py flask init-db
cp flag.db flagtests.db
```

After the database has been created:

    FLASK_APP=app.py FLASK_ENV=development flask run

### Running tests

    pytest -s --verbose

### To look at the database

`pip install datasette` first if needed
`datasette flag.db`


click the link (typically port 8001 on localhost)

or run `sqlite`

### To Deploy to Heroku

```

heroku create
heroku git:remote -a codefordc-flag
heroku config:set FLASK_APP=app.py FLASK_ENV=development
heroku run flask db init
heroku run flask db migrate
heroku run flask db upgrade
```

### TODOs:

- Plug some data in there along lines of the [Figma](https://www.figma.com/file/Lzq30lUA6N0hevjn8JVU6z/flag-requests)


## Ensemble Programming Environment

- https://mobti.me/flagpizza
- https://anydesk.com
