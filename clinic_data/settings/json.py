from django.core.exceptions import ImproperlyConfigured
import json

with open("secret.json") as f:
    secret=json.loads(f.read())

def getSecret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = f"The variable {secret_name} doesn't exit"
        raise ImproperlyConfigured(msg)

