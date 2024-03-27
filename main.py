from dotenv import load_dotenv
import os
import requests

# Chargez les variables d'environnement
load_dotenv()

# Variables pour l'API Zoho CRM
ZOHO_CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
ZOHO_CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
ZOHO_REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")
access_token = os.getenv("ZOHO_ACCESS_TOKEN")
print("Access Token:", access_token)

def refresh_access_token():
    """Rafraîchit le token d'accès en utilisant le refresh token."""
    refresh_url = "https://accounts.zoho.com/oauth/v2/token"
    params = {
        'refresh_token': ZOHO_REFRESH_TOKEN,
        'client_id': ZOHO_CLIENT_ID,
        'client_secret': ZOHO_CLIENT_SECRET,
        'grant_type': 'refresh_token'
    }
    response = requests.post(refresh_url, data=params, timeout=10)
    if response.status_code == 200:
        new_access_token = response.json().get('access_token')
        print("Token d'accès rafraîchi avec succès.")
        return new_access_token
    else:
        print("Échec du rafraîchissement du token d'accès.")
        return None

def get_cat_breeds():
    """Récupère les races de chats dont l'origine est 'Natural'."""
    response = requests.get("https://catfact.ninja/breeds", timeout=10)
    response.raise_for_status()
    breeds = response.json()["data"]
    return [breed for breed in breeds if 'Natural' in breed["origin"]]

def create_contact_in_zoho(access_token, breed_name):
    """Crée un contact dans Zoho CRM."""
    headers = {
        'Authorization': f'Zoho-oauthtoken {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        "data": [{
            "First_Name": breed_name,
            "Last_Name": breed_name,
            "Email": f"{breed_name.replace(' ', '_')}@gmail.com"
        }]
    }
    response = requests.post("https://www.zohoapis.com/crm/v2/Contacts", json=data, headers=headers, timeout=10)
    if response.status_code in [200, 201]:
        print(f"Contact pour {breed_name} créé avec succès.")
    else:
        print(f"Erreur lors de la création du contact pour {breed_name}: {response.text}")

def main():
    """Point d'entrée principal du script."""
    access_token = refresh_access_token() 
    cat_breeds = get_cat_breeds()
    for breed in cat_breeds:
        create_contact_in_zoho(access_token, breed['breed'])


if __name__ == "__main__":
    main()
