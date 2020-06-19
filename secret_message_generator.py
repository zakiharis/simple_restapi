import base64
import requests

from jwcrypto import jwk, jwe
from jwcrypto.common import json_decode

print('Please enter API domain (http://127.0.0.1:5000)')
DOMAIN = str(input())

if not DOMAIN:
    DOMAIN = 'http://127.0.0.1:5000'

# login
resp = requests.post(DOMAIN + '/auth/login', json={'email': 'admin1234@admin.my', 'password': 'admin1234'})
access_token = resp.json()['data']['access_token']

# get pub key
resp = requests.get(DOMAIN + '/auth/key', headers={'Authorization': 'Bearer ' + access_token})
pub_key = resp.json()['data']['public_key']
public_key = jwk.JWK()
public_key.import_key(**json_decode(pub_key))

# generate secret message
print('Please enter your secret message..')
payload = str(input())
protected_header = {
    'alg': 'RSA-OAEP-256',
    'enc': 'A256CBC-HS512',
    'typ': 'JWE',
    'kid': public_key.thumbprint(),
}
jwetoken = jwe.JWE(payload.encode('utf-8'), recipient=public_key, protected=protected_header)
enc = jwetoken.serialize()
b64enc = base64.b64encode(enc.encode('ascii'))

json = '{"encrypted_message": "' + b64enc.decode('ascii') + '"}'
print('Send below payload to /auth/decode to verify secret message')
print(json)
