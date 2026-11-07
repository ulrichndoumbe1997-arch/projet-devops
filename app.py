
from flask import Flask

# Création de l'application Flask
app = Flask(__name__)

# Route de la page d'accueil
@app.route("/")
def accueil():
    return """
    <h1>Bienvenue dans mon premier projet DevOps !</h1>
    <p>Mon application Python fonctionne correctement.</p>
    <p>Nous allons automatiser son déploiement avec Jenkins et Docker.</p>
    """

# Démarrage du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
