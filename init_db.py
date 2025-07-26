from app import app, db
from models import Utilisateur  # même si grisé, à garder

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("✅ Tables créées avec succès !")
