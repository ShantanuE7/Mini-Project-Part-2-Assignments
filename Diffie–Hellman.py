def generate_public_key(private_key, g, p):
    # Calculate the public key (g^private_key mod p)
    return pow(g, private_key, p)

def calculate_shared_secret(private_key, received_public_key, p):
    # Calculate the shared secret (received_public_key^private_key mod p)
    return pow(received_public_key, private_key, p)

def main():
    # Input prime number and primitive root
    p = int(input("Enter the prime number (p): "))
    g = int(input("Enter the primitive root (g): "))
    
    # Input private keys for Alice and Bob
    alice_private_key = int(input("Enter Alice's private key (a): "))
    bob_private_key = int(input("Enter Bob's private key (b): "))
    
    # Calculate public keys
    alice_public_key = generate_public_key(alice_private_key, g, p)
    bob_public_key = generate_public_key(bob_private_key, g, p)
    
    print("\nAlice's public key:", alice_public_key)
    print("Bob's public key:", bob_public_key)
    
    # Alice and Bob calculate the shared secret
    alice_shared_secret = calculate_shared_secret(alice_private_key, bob_public_key, p)
    bob_shared_secret = calculate_shared_secret(bob_private_key, alice_public_key, p)
    
    # Both Alice and Bob should have the same shared secret
    if alice_shared_secret == bob_shared_secret:
        print("\nShared secret established successfully!")
        print("Shared secret:", alice_shared_secret)
    else:
        print("\nError: Shared secret mismatch!")

if __name__ == "__main__":
    main()

"""
OUTPUT:

Enter the prime number (p): 13
Enter the primitive root (g): 7
Enter Alice's private key (a): 5
Enter Bob's private key (b): 3

Alice's public key: 11
Bob's public key: 5

Shared secret established successfully!
Shared secret: 5

"""