# Image de base légère avec Python 3.11
FROM python:3.11-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'app dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Rendre les variables d'environnement accessibles (Render les injecte automatiquement)
ENV PYTHONUNBUFFERED=1

# Exposer le port utilisé par gunicorn
EXPOSE 8000

# Commande de démarrage de l'application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
