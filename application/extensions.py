from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate



# initialize our database and marshmallow
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()