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
    pip install -r requirements.txt
    

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

# Running tests

    pytest -s --verbose

# Viewing Data

`pip install datasette` first if needed
`datasette flag.db`


click the link (typically port 8001 on localhost)

or run `sqlite`

### Deploying to Heroku

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
