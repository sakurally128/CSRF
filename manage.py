from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from models import User
from app import app
from exts import db


manger = Manager(app)

migrate = Migrate(app,db)
manger.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manger.run()