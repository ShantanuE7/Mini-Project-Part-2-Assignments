import random
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(bits):
    while True:
        n = random.getrandbits(bits)
        if is_prime(n):
            return n

def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = pow(e, -1, phi)

    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    return ' '.join([str(pow(ord(char), e, n)) for char in message])

def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(int(char), d, n)) for char in ciphertext.split()])

def main():
    while True:
        print("\nRSA Menu:")
        print("1. Generate Key Pair")
        print("2. Encrypt Message")
        print("3. Decrypt Ciphertext")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            bits = int(input("Enter the number of bits for the key pair (recommended: 1024 or higher): "))
            public_key, private_key = generate_keypair(bits)
            print("Public Key (e, n):", public_key)
            print("Private Key (d, n):", private_key)
        elif choice == '2':
            message = input("Enter the message to encrypt: ")
            public_key = tuple(map(int, input("Enter the public key (e, n): ").split(',')))
            encrypted_message = encrypt(message, public_key)
            print("Encrypted Message:", encrypted_message)
        elif choice == '3':
            ciphertext = input("Enter the ciphertext (space-separated integers): ")
            private_key = tuple(map(int, input("Enter the private key (d, n): ").split(',')))
            decrypted_message = decrypt(ciphertext, private_key)
            print("Decrypted Message:", decrypted_message)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
