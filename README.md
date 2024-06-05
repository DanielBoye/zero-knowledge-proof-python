# Zero-Knowledge Proof Python

Zero-knowledge proofs are a type of cryptographic protocol that enables a prover to convince a verifier that they possess certain knowledge or information without revealing the actual knowledge or information itself

## Definitions and Notation

Let:
- $H(x)$ be a cryptographic hash function (e.g., SHA-256).
- $s$ be the secret known to the prover.
- $N$ be a predefined constant, representing the range of random values.
- $salt$ be a random string to ensure uniqueness and prevent precomputed attacks.
- $r$ be a random value chosen by the prover.
- $v$ be the verifier's value, computed by hashing the secret.
- $x$ be the prover's commitment, computed by hashing the random value.

## Proof Generation (Prover's Part)

1. The prover computes $v$ as:
   $v = H(s | salt)$
   where $|$ denotes concatenation.

2. The prover generates a random value $r$:
   $r \in \{1, 2, \ldots, N\}$


3. The prover computes the commitment $x$ as:
   $x = H(r | salt)$

4. The prover sends the commitment $x$ to the verifier.

## Verification (Verifier's Part)

1. The verifier receives the prover's response, which should be the secret $s$.

2. The verifier computes:

   $H(response| salt)$

   where `response` is the value received from the prover.

3. The verifier checks if:

   $v = H(response | salt)$

If the equation holds, the verifier confirms that the prover knows the secret $s$ without the secret being revealed.

## Properties and Security

- The **salt** ensures that each hash is unique, preventing rainbow table attacks.
- The random value $r$ introduces randomness, making each commitment $x$ unique, even if the same secret is used multiple times.
- The hash function $H(x)$ is one-way, making it infeasible to retrieve $s$ or $r$ from $v$ or $x$.

## Python Implementation

```python
import hashlib
import os
import random

N = 20
salt = os.urandom(16)

def _hash(x, salt):
    return hashlib.sha256(x.encode('utf-8') + salt).hexdigest()

def generate_proof(secret, salt):
    v = _hash(secret, salt)
    r = str(random.randint(1, N))
    x = _hash(r, salt)
    return x, v, secret

def verify(v, response, salt):
    return v == _hash(response, salt)

secret = 'my_secret'  # Here we define the secret
x, v, secret = generate_proof(secret, salt)
print('Proof:', x)

response = input('Enter the card to verify: ')
print('Verified:', verify(v, response, salt))
```
## How to Run the Python File

1. Make sure you have Python installed on your system.

2. Save the provided Python code into a file, for example, main.py.

3. Open your terminal or command prompt.

4. Navigate to the directory where you saved the zkp.py file.

5. Run the script by typing:

`python zkp.py`

6. The script will print a proof of the secret you set to verify.

7. The script will then output whether the verification was successful.
