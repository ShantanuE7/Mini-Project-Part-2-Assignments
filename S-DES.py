# S-DES

def key_generation():
    key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]

    key_ = [key[i - 1] for i in P10]
    Ls = key_[:5]
    Rs = key_[5:]
    
    Ls_1 = shift(Ls, 1)
    Rs_1 = shift(Rs, 1)
    key1 = generate_key(Ls_1, Rs_1, P8)
    
    Ls_2 = shift(Ls, 2)
    Rs_2 = shift(Rs, 2)
    key2 = generate_key(Ls_2, Rs_2, P8)
    
    return key1, key2

def shift(ar, n):
    return ar[n:] + ar[:n]

def generate_key(Ls, Rs, P8):
    key_ = Ls + Rs
    return [key_[i - 1] for i in P8]

def binary_(val):
    if val == 0:
        return "00"
    elif val == 1:
        return "01"
    elif val == 2:
        return "10"
    else:
        return "11"

def function_(ar, key_):
    EP = [4, 1, 2, 3, 2, 3, 4, 1]
    P4 = [2, 4, 3, 1]
    S0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
    ]
    S1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
    ]

    l = ar[:4]
    r = ar[4:]
    ep = [r[i - 1] for i in EP]
    ar = [key_[i] ^ ep[i] for i in range(8)]
    l_1 = ar[:4]
    r_1 = ar[4:]
    row = int(str(l_1[0]) + str(l_1[3]), 2)
    col = int(str(l_1[1]) + str(l_1[2]), 2)
    val = S0[row][col]
    str_l = binary_(val)
    row = int(str(r_1[0]) + str(r_1[3]), 2)
    col = int(str(r_1[1]) + str(r_1[2]), 2)
    val = S1[row][col]
    str_r = binary_(val)
    r_ = [int(str_l[i]) for i in range(2)] + [int(str_r[i]) for i in range(2)]
    r_p4 = [r_[i - 1] for i in P4]
    l = [l[i] ^ r_p4[i] for i in range(4)]
    output = l + r_
    return output

def swap(array, n):
    l = array[:n]
    r = array[n:]
    output = r + l
    return output

def encryption(plaintext):
    key1, key2 = key_generation()
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]

    arr = [plaintext[i - 1] for i in IP]
    arr1 = function_(arr, key1)
    after_swap = swap(arr1, len(arr1) // 2)
    arr2 = function_(after_swap, key2)
    ciphertext = [arr2[i - 1] for i in IP_inv]
    return ciphertext

def decryption(ciphertext):
    key1, key2 = key_generation()
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]

    arr = [ciphertext[i - 1] for i in IP]
    arr1 = function_(arr, key2)
    after_swap = swap(arr1, len(arr1) // 2)
    arr2 = function_(after_swap, key1)
    decrypted = [arr2[i - 1] for i in IP_inv]
    return decrypted

def main():
    plaintext = input("Enter 8-bit plaintext (e.g., 10010111): ")
    if len(plaintext) != 8 or not all(bit in '01' for bit in plaintext):
        print("Please enter a valid 8-bit binary plaintext.")
        return

    plaintext = [int(bit) for bit in plaintext]
    print("Your plain Text is :", plaintext)
    
    ciphertext = encryption(plaintext)
    print("Your cipher Text is :", ciphertext)
    
    decrypted = decryption(ciphertext)
    print("Your decrypted Text is :", decrypted)

if __name__ == "__main__":
    main()

"""
OUTPUT:

Enter 8-bit plaintext (e.g., 10010111): 10111100
Your plain Text is : [1, 0, 1, 1, 1, 1, 0, 0]
Your cipher Text is : [0, 0, 1, 0, 0, 0, 0, 1]
Your decrypted Text is : [1, 0, 1, 1, 1, 1, 0, 0]

"""
  
