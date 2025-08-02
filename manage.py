from app import app, db
from flask_migrate import Migrate
from flask.cli import with_appcontext
import click

migrate = Migrate(app, db)

# (Optionnel) Commande custom pour créer les tables rapidement
@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()

app.cli.add_command(create_tables)
