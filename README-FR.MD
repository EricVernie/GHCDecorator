## Méthode decode_token

La méthode `decode_token` est utilisée pour décoder les JWT (JSON Web Tokens). Elle utilise la bibliothèque `jose` pour effectuer ce décodage.

### Utilisation

```python
decode_token(token)
```

Paramètres

token : </b>
Le JWT à décoder. Il s'agit d'une chaîne de caractères.

Retour </b>

La méthode retourne un dictionnaire contenant les informations décodées du token si le token est valide. Si le token n'est pas valide, une exception est levée.

Exemple </b>
```python 
try:
    data = decode_token(my_token)
    print("Les données décodées du token sont :", data)
except Exception as e:
    print("Une erreur est survenue lors du décodage du token :", e)
```




## Méthode validate_token

La méthode `validate_token` est un décorateur utilisé pour valider les JWT (JSON Web Tokens). Elle utilise la bibliothèque `jose` pour effectuer cette validation.

### Utilisation

```python
@validate_token
def ma_fonction():
    # Votre code ici
```

### Paramètres

- `token` : Le JWT à valider. Il s'agit d'une chaîne de caractères.

### Retour

La méthode retourne `True` si le token est valide, `False` sinon. Si le token n'est pas valide, la fonction décorée n'est pas exécutée.

### Exemple

```python
@validate_token
def ma_fonction():
    print("Cette fonction ne s'exécute que si le token est valide.")

try:
    ma_fonction()
except Exception as e:
    print("Une erreur est survenue :", e)
```
Dans cet exemple, `ma_fonction` ne s'exécute que si le token passé à `validate_token` est valide. Si le token n'est pas valide, une exception est levée.
