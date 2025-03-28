# Schema migration with Flask

This template workspace gives the project structure to setup a flask web application, using SQLAlchemy, Flask-Migrate, Flask-Marshmallow and Pytest.

Alembic migrations are stored in the `migrations` folder by default.

This project was inspired and follows the same structure as another Flask example made by the youtuber Eduardo Mendes. My goal is to expand with more advanced configurations, including Docker and CI/CD.

[Original video](https://youtu.be/WzaKIRJBGXo)

[His Youtube Channel](https://www.youtube.com/@Dunossauro)

[Source Code](https://github.com/dunossauro/crudzin)

## Project Structure

This project features an flask app, defined as a package in the **\_\_init\_\_.py** file, the function `create_app` act as application factory and is automatically detected when `flask run` is executed (see the [Flask tutorial](https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/) for more details).

All database tables are expressed as classes in the **models.py** file, the function to setup the database is also defined in this file.

**serializer.py** contains the schemas to serialize every model.

**hello_world.py** defines a blueprint, which contains its own set of routes that can be registered to the app.

Lastly. the html that is rendered on the starting route is included in the
**templates** folder

## Configure Development Workspace

1. Set the environment variables

You can either add all your variables in a `.env` file or export them in a single terminal session.

You can create a secret key with the following command:

```console
 openssl rand -hex 64
```

Then write on the .env file:

```.env
DATABASE_URI="<your_database_uri_here>"
SECRET_KEY="<your_secret_key>"
```

Or export on the terminal session:

- **Linux**

```shell
export DATABASE_URI="<your_database_uri_here>"
export SECRET_KEY="<your_secret_key>"
```

- **Windows**

```cmd
setx DATABASE_URI="<your_database_uri_here>"
setx SECRET_KEY="<your_secret_key>"
```

2. Install dev_requirements

```shell
pip install -r dev_requirements.txt
```

3. Upgrade the database to latest migration

`flask db upgrade`

4. Configure your self-signed ssl certificate for the development environment

To create a self signed certificate you can execute this openssl command:

```shell
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365 
```

You can answer the questions made with . (blank) or any value you prefer, it will be used only on development.

5. Run the app locally 

`flask run --debug --cert cert.pem --key key.pem`

## TODO

- [x] Containerize the application
- [x] Set up dependabot
- [ ] Configure docker compose with Nginx
- [ ] Configure logging
- [ ] Style the hello page
