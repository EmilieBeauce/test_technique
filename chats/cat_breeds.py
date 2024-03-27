import requests

def get_cat_breeds():
    """Récupère les races de chats dont l'origine est 'Natural'."""
    response = requests.get("https://catfact.ninja/breeds", timeout=10)
    response.raise_for_status()
    breeds = response.json()["data"]
    return [breed for breed in breeds if 'Natural' in breed["origin"]]
