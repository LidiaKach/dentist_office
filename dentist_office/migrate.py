from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dentist_office.run import create_app
from dentist_office.models import db

app = create_app('dentist_office.config')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from dentist_office.models import *

if __name__ == '__main__':
    manager.run()
