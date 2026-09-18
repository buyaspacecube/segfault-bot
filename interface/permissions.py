from discord import Permissions

from dotenv import load_dotenv
from os import getenv

def _get_permissions_if_playtesting():

    load_dotenv()

    if getenv('PLAYTESTING') == '1':
        return Permissions(create_private_threads = True)

    return Permissions()

def get_base_permissions():
    
    perms = Permissions() + _get_permissions_if_playtesting()

    if perms.value == 0:
        return None
    
    return perms

def get_referee_permissions():
    
    perms = Permissions(create_public_threads = True) + _get_permissions_if_playtesting()
    
    if perms.value == 0:
        return None
    
    return perms

def get_admin_permissions():
    return Permissions(administrator = True)
