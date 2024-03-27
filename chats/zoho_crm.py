import requests
from config import get_config

def create_contact_in_zoho(breed_name):
    """Crée un contact dans Zoho CRM."""
    configs = get_config()
    access_token = configs['ZOHO_REFRESH_TOKEN']
    if access_token:
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
    else:
        print("Token d'accès non disponible.")
