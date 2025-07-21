# Utiliser Python 3.11 comme image de base
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code de l'application
COPY . .

# Exposer le port 8090
EXPOSE 8090

# Définir les variables d'environnement
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Commande pour démarrer l'application avec Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8090", "--workers", "4", "app:app"]

