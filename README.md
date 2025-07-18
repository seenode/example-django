# Deploy Django on Seenode in seconds

This is a sample repository for deploying a Django project on [Seenode](https://seenode.com).

It includes a single "Hello, World" view and is pre-configured to be served with Gunicorn, the recommended production-ready web server.

### Deploy in minutes
View our [guide on deploying Django apps](https://seenode.com/docs/frameworks/python/django/) on [Seenode](https://seenode.com).


## Deploying on Seenode

1.  **Create Service**: From the [Seenode dashboard](https://cloud.seenode.com), create a new **Web Service** and connect it to this Git repository.
2.  **Configure Settings**: In your service settings on Seenode, make sure the following are set:
    *   **Build Command**: `pip install -r requirements.txt`
    *   **Start Command**: `gunicorn project.wsgi --bind 0.0.0.0:$PORT`
3.  **Add Environment Variables**: In your service's **Environment** tab, add the following:
    *   `SECRET_KEY`: A long, random string for cryptographic signing.
    *   `DEBUG`: Set to `False` for production.
4.  **Deploy**: Click **Create Web Service** or **Deploy** to apply the changes. Your app will be live shortly.

### Connecting a Database

Seenode simplifies database management.
1.  Create a managed PostgreSQL or MySQL database from the **Databases** tab on the dashboard.
2.  In your Web Service settings, go to the **Environment** tab.
3.  Under "Database Connections", link your newly created database.
4.  Seenode will automatically inject the `DATABASE_URL` environment variable directly into your service, which Django can use to connect securely.


***
