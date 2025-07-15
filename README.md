# Django Sample Project

This is a minimal Django project intended to be used as a sample for deployment guides.
It contains a single app with a view that returns a simple "Hello, world" message.

The project is configured to be served using gunicorn.

## Configuration

The project is configured using environment variables. You will need to set the following:

- `SECRET_KEY`: A long, random string used for cryptographic signing.
- `DEBUG`: Set to `True` for development, `False` for production. Defaults to `False`.
- `DATABASE_URL`: The connection string for your database. Defaults to a local SQLite database.

For local development, you can set these in your shell:

```bash
export SECRET_KEY='a-very-secret-key'
export DEBUG=True
export DATABASE_URL='sqlite:///db.sqlite3'
``` 