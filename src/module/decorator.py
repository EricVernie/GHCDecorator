# Le décorateur doit valider le scope User_Impersonation
# Si le scope n'est pas présent dans le Jeton d'accès, le décorateur doit retourner une erreur 403
# Si le scope est présent, le décorateur doit appeler la méthode read_token 
# Vérifier dans le jeton la présence du claim roles 
# Vérifier si dans le jeton il y a la présence du rôle passé en paramètre
# Si le rôle n'est pas présent, le décorateur doit retourner une erreur 403
# Si le rôle est présent, le décorateur doit appeler la méthode passée en paramètre

from functools import wraps
from flask import request, abort
from module.decodetoken import decode_token
from typing import Dict

def validate_token(role):
    """
    Décorateur qui valide le jeton d'authentification et vérifie le rôle de l'utilisateur.

    Args:
        role (str): Le rôle requis pour accéder à la fonction décorée.

    Returns:
        function: La fonction décorée qui vérifie le jeton et le rôle de l'utilisateur.
    """
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token: str = request.headers.get('Authorization').replace('Bearer ', '')
            if not token:
                abort(403, description="No token provided")
            
            # Ici, vous devriez ajouter le code pour décoder et vérifier le jeton.
            # Pour cet exemple, nous supposons que vous avez une fonction `decode_token` qui fait cela.
            
            decoded_token: Dict[str,str] = decode_token(token)
            if not decoded_token:
                abort(403, description="Invalid token")
            # TODO: Faire un test sur la casse des scopes et des roles
            if 'User_Impersonation' not in decoded_token['scp']:
                abort(403, description="User_Impersonation scope required")
            
            if role not in decoded_token['roles']:
                abort(403, description=f"Role {role} required")

            return func(*args, **kwargs)
        return wrapper
    return decorator


