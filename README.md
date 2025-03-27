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

1. Set the `DATABASE_URI` environment variable

- **Linux**

```shell
export DATABASE_URI="your_database_uri_here"
```

- **Windows**

```cmd
setx DATABASE_URI="your_database_uri_here"
```

2. Install dev_requirements

```shell
pip install -r dev_requirements.txt
```

3. Upgrade the database to latest migration

`flask db upgrade`

4. Run the app

`flask run --debug`

## TODO

- [x] Containerize the application
- [x] Set up dependabot
- [ ] Create actions workflow for migrations
- [ ] Configure logging
- [ ] Style the hello page
