# settings.py
CLIENT_ID               = "27f978d3-f3ea-4eba-9329-04d4e1ff3fba"
TENANT_ID               = "312e8fa5-668a-4188-91bf-86b88d0c392a"
SCOPE                   = "User_Impersonation"
# JWT settings
JWT_ALGORITHMS          = ["RS256"]
JWT_PUBLIC_KEY_URL      = "https://login.microsoftonline.com/common/discovery/keys"
VERIFY_EXP              = False
VERIFY_AUDIENCE         = False
VERIFY_ISSUER           = False
VERIFY_NBF              = False
REQUIRED_EXP            = False
REQUIRED_IAT            = False
REQUIRED_SUB            = False
REQUIRED_NBF            = False
AUDIENCE                = "27f978d3-f3ea-4eba-9329-04d4e1ff3fba"
ISSUER                  = "https://login.microsoftonline.com/312e8fa5-668a-4188-91bf-86b88d0c392a/v2.0"
# END