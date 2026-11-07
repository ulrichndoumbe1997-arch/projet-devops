from app import app

def test_page_accueil():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Bienvenue dans mon premier projet DevOps !" in response.data