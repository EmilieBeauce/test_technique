import logging
import requests
from config import get_config


# Configuration du logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def refresh_access_token():
    """Rafraîchit le token d'accès en utilisant le refresh token."""
    configs = get_config()
    refresh_url = "https://accounts.zoho.com/oauth/v2/token"
    params = {
        'refresh_token': configs['ZOHO_REFRESH_TOKEN'],
        'client_id': configs['ZOHO_CLIENT_ID'],
        'client_secret': configs['ZOHO_CLIENT_SECRET'],
    }
    try:
        response = requests.post(refresh_url, data=params, timeout=10)
        response.raise_for_status()
        return response.json().get('access_token')
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"Erreur HTTP lors du rafraîchissement du token d'accès: {http_err}")
    except Exception as err:
        logging.error(f"Une erreur s'est produite lors du rafraîchissement du token d'accès: {err}")
    return None
