# Méthode qui décode un jeton JWT
# Ce jeton est un jeton provenant d'Azure Active Directory
# La méthode devra récupérer la clé publique via le point d'entré https://login.microsoftonline.com/common/discovery/keys
# et devra utiliser l'algorithme RS256 pour décoder le jeton
# Il devra également invalider le jeton si la date est dépassée, si l'audience ou l'issuer ne correspond pas à la configuration

import requests
import settings
from jose import jwt
from jose.exceptions import JWTError
from typing import Dict, Any

__all__ = ['decode_token']

def decode_token(token):
    # Récupérer les clés publiques
    jwks_uri:  str = "https://login.microsoftonline.com/common/discovery/keys"
    response = requests.get(jwks_uri)
    jwks = response.json()
    try:
        # Décoder le jeton
        
        header: Dict[str, str] = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        
        decoded_token: Dict[str, str] = jwt.decode(token, 
                                    rsa_key, 
                                    algorithms=settings.JWT_ALGORITHMS,
                                    audience=settings.AUDIENCE,
                                    issuer=settings.ISSUER,
                                    options={"verify_exp"        : settings.VERIFY_EXP,
                                                "verify_aud"     : settings.VERIFY_AUDIENCE,
                                                "verify_iss"     : settings.VERIFY_ISSUER,
                                                "verified_nbf"   : settings.VERIFY_NBF,
                                                "require_exp"    : settings.REQUIRED_EXP,
                                                "require_iat"    : settings.REQUIRED_IAT,
                                                "require_sub"    : settings.REQUIRED_SUB,
                                                "require_nbf"    : settings.REQUIRED_NBF,
                                                })   

        return decoded_token
    except JWTError:
        # Le jeton est invalide
        return None