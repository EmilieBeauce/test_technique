from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from dotenv import load_dotenv
import os

load_dotenv()

def get_config():
    """Récupère les configurations à partir des variables d'environnement."""
    return {
        'client_id': os.getenv("ZOHO_CLIENT_ID"),
        'client_secret': os.getenv("ZOHO_CLIENT_SECRET"),
        'refresh_token': os.getenv("ZOHO_REFRESH_TOKEN"),
    }

def get_api_environment():
    """
    Configure et retourne l'environnement de l'API.
    """
    return USDataCenter.PRODUCTION()

def initialize_sdk():
    """
    Initialise le SDK Zoho CRM avec la configuration requise.
    """
    configs = get_config()  # Supposons que cette fonction extrait les autres configs nécessaires
    environment = get_api_environment()

    token = OAuthToken(client_id=configs['client_id'],
                       client_secret=configs['client_secret'],
                       refresh_token=configs['refresh_token'])

    Initializer.initialize(environment=environment, token=token)

if __name__ == "__main__":
    initialize_sdk()

