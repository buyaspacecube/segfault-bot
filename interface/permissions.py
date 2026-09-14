from discord import Permissions

from dotenv import load_dotenv
from os import getenv

def _get_permissions_if_playtesting():

    load_dotenv()

    if getenv('PLAYTESTING') == 1:
        return Permissions(create_private_threads = True)

    return Permissions()

def get_base_permissions():
    return Permissions() + _get_permissions_if_playtesting()

def get_referee_permissions():
    return Permissions(create_public_threads = True) + _get_permissions_if_playtesting()

def get_admin_permissions():
    return Permissions(administrator = True)
