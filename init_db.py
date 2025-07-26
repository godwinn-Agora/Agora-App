from app import app, db
from models import Utilisateur  # même si grisé, à garder


with app.app_context():
    db.create_all()
    print("✅ Tables créées avec succès !")
