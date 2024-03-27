from dotenv import load_dotenv
from chats.cat_breeds import get_cat_breeds
from chats.zoho_crm import create_contact_in_zoho
load_dotenv()


def main():
    '''fonction principale pour créer des contacts dans le crm.'''
    cat_breeds = get_cat_breeds()
    for breed in cat_breeds:
        create_contact_in_zoho(breed['breed'])

if __name__ == "__main__":
    main()
