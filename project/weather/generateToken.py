#!/usr/bin/env python3
import sys
import time

import jwt

# Open PEM
private_key = """-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIPEbnYSWS+arsaMqRQ3WMNDK/quw0bLTqG9qZxeDC4hj
-----END PRIVATE KEY-----"""

payload = {
    'iat': int(time.time()) - 30,
    'exp': int(time.time()) + 900,
    'sub': '258BR4VM99'
}
headers = {
    'kid': 'YOUR_TGGVD7RTJYKEY_ID'
}

# Generate JWT
encoded_jwt = jwt.encode(payload, private_key, algorithm='EdDSA', headers = headers)

print(f"JWT:  {encoded_jwt}")