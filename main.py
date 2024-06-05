import hashlib
import os
import random

N = 20
salt = os.urandom(16)

def hash(x, salt):
    return hashlib.sha256(x.encode('utf-8') + salt).hexdigest()

def generate_proof(secret, salt):
    v = hash(secret, salt)
    r = str(random.randint(1, N))
    x = hash(r, salt)
    return x, v, secret

def verify(v, response, salt):
    return v == hash(response, salt)

secret = 'my_secret'  # Here we define the secret
x, v, secret = generate_proof(secret, salt)
print('Proof:', x)

response = input('Enter the proof to verify: ')
print('Verified:', verify(v, response, salt))
