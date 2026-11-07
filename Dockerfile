# Image de base Python
FROM python:3.12-slim

# Définir le dossier de travail
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app.py .

# Exposer le port de l'application
EXPOSE 5000

# Lancer l'application Flask
CMD ["python", "app.py"]