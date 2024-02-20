from flask_marshmallow import Marshmallow

from .models import Person

ma = Marshmallow()

def config_ma(app):
    ma.init_app(app)


class PersonSchema(ma.Schema):
    class Meta:
        model = Person
    