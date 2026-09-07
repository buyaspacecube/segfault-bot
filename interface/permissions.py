from discord import Permissions

def get_referee_permissions():
    return Permissions(create_public_threads = True)

def get_admin_permissions():
    return Permissions(administrator = True)
