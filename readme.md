# Capitol Flag Pizza Tracker App

In collaboration with Modernization Staff Association.

Flask app proof of concept.

To run:
TODO: https://dev.to/mburszley/an-introduction-to-poetry-2b6n ?

If using conda:

    If environment not set up before:
    ```
    conda create --name myenv
    ```

    Next:
    ```
    conda activate myenv
    pip install -r requirements.txt
    ```

OR if using python

    If you have not already set up your python env
    ```
    python3 -m venv myenv
    ```

    Next:

    ```
    source myenv/bin/activate
    pip install -r requirements.txt
    ```

If database is not created in your local environment:

`DEBUG=True FLASK_APP=app.py flask db init`

If database is created but you want to recreate
`git checkout ./migrations`
`DEBUG=True FLASK_APP=app.py flask db init`
DEBUG=True FLASK_APP=app.py flask db migrate
DEBUG=True FLASK_APP=app.py flask db upgrade

After the database has been created:

``
FLASK_APP=app.py FLASK_ENV=development flask run

```

### Running tests

```

pytest -s --verbose

```

### To look at the database

`pip install datasette` first if needed
`datasette flag.db`
click the link (typically port 8001 on localhost)

or run `sqlite`

### To Deploy to Heroku
```

heroku create
heroku buildpacks:add --index 1 heroku-community/apt
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

```

```

```
