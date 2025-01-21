#pip install cryptography #In the Terminal before running the below

from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

# Step 1: Generate Parameters (Prime p and Generator g)
def generate_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    return parameters

# Step 2: Alice's Side (Private Key, Public Key)
def alice_key_exchange(parameters):
    # Alice generates her private key
    alice_private_key = parameters.generate_private_key()
    # Alice generates her public key from the private key
    alice_public_key = alice_private_key.public_key()
    return alice_private_key, alice_public_key

# Step 3: Bob's Side (Private Key, Public Key)
def bob_key_exchange(parameters):
    # Bob generates his private key
    bob_private_key = parameters.generate_private_key()
    # Bob generates his public key from the private key
    bob_public_key = bob_private_key.public_key()
    return bob_private_key, bob_public_key

# Step 4: Shared Secret Computation (Alice and Bob)
def compute_shared_secret(private_key, public_key):
    # Compute shared secret using the private key of one party and the public key of the other
    shared_secret = private_key.exchange(public_key)
    return shared_secret

def main():
    # Step 1: Generate shared parameters (same for both Alice and Bob)
    parameters = generate_parameters()
    
    # Step 2: Alice and Bob exchange keys
    alice_private_key, alice_public_key = alice_key_exchange(parameters)
    bob_private_key, bob_public_key = bob_key_exchange(parameters)
    
    # Serialize and print public keys
    alice_public_key_bytes = alice_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    bob_public_key_bytes = bob_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    print("Alice's Public Key:\n", alice_public_key_bytes.decode())
    print("Bob's Public Key:\n", bob_public_key_bytes.decode())

    # Step 3: Exchange public keys (simulate communication over insecure channel)
    # Alice computes the shared secret using her private key and Bob's public key
    alice_shared_secret = compute_shared_secret(alice_private_key, bob_public_key)
    # Bob computes the shared secret using his private key and Alice's public key
    bob_shared_secret = compute_shared_secret(bob_private_key, alice_public_key)
    
    # Step 4: Verify both secrets match
    if alice_shared_secret == bob_shared_secret:
        print("\nShared Secret Computation Successful!")
        print("Shared Secret (hex):", alice_shared_secret.hex())
    else:
        print("\nShared Secrets do not match!")

if __name__ == '__main__':
    main()
