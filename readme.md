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

If database is not created in your local environment or you want to recreate:

If you already setup: `rm flag.db`

```
DEBUG=True FLASK_APP=app.py flask db init
DEBUG=True FLASK_APP=app.py flask db migrate
DEBUG=True FLASK_APP=app.py flask db upgrade

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

### TODOs:

- Plug some data in there along lines of the (https://www.figma.com/file/Lzq30lUA6N0hevjn8JVU6z/flag-requests?node-id=2%3A4)[Figma]

## Ensemble Programming Environment

- https://mobti.me/flagpizza
- https://anydesk.com

```

```
