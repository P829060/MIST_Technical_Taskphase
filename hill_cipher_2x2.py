#!/usr/bin/env python3
# hill_cipher_2x2.py
# Small Hill Cipher tool: encrypt, decrypt and brute-force (2x2 key)

from math import gcd
from itertools import product

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
M = 26

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a, m):
    g, x, _ = egcd(a % m, m)
    if g != 1:
        return None
    return x % m

def matrix_det_2x2(mat):
    return (mat[0]*mat[3] - mat[1]*mat[2]) % M

def matrix_inv_2x2(mat):
    det = matrix_det_2x2(mat)
    inv_det = modinv(det, M)
    if inv_det is None:
        return None
    a, b, c, d = mat
    inv = [( d * inv_det) % M,
           ((-b) * inv_det) % M,
           ((-c) * inv_det) % M,
            ( a * inv_det) % M]
    return inv

def text_to_numbers(text):
    return [ALPHABET.index(ch) for ch in text.upper() if ch.isalpha()]

def numbers_to_text(nums):
    return "".join(ALPHABET[n % M] for n in nums)

def pad_text(text, block_size=2, pad_char='X'):
    filtered = "".join(ch for ch in text.upper() if ch.isalpha())
    if len(filtered) % block_size != 0:
        filtered += pad_char * (block_size - (len(filtered) % block_size))
    return filtered

def encrypt_block(block_nums, key):
    a,b,c,d = key
    x, y = block_nums
    return [(a*x + b*y) % M, (c*x + d*y) % M]

def decrypt_block(block_nums, key_inv):
    return encrypt_block(block_nums, key_inv)

def encrypt(plaintext, key):
    block_size = 2
    pt = pad_text(plaintext, block_size)
    nums = text_to_numbers(pt)
    cipher_nums = []
    for i in range(0, len(nums), block_size):
        block = nums[i:i+block_size]
        cipher_nums.extend(encrypt_block(block, key))
    return numbers_to_text(cipher_nums)

def decrypt(ciphertext, key):
    nums = text_to_numbers(ciphertext)
    inv = matrix_inv_2x2(key)
    if inv is None:
        raise ValueError("Key is not invertible mod 26; can't decrypt.")
    plain_nums = []
    for i in range(0, len(nums), 2):
        block = nums[i:i+2]
        plain_nums.extend(decrypt_block(block, inv))
    return numbers_to_text(plain_nums).rstrip('X')

def all_invertible_2x2_keys():
    for a, b, c, d in product(range(M), repeat=4):
        det = (a*d - b*c) % M
        if gcd(det, M) == 1:
            yield [a,b,c,d]

def brute_force_known_plaintext(ciphertext, known_plaintext):
    ct = pad_text(ciphertext, 2)
    pt = pad_text(known_plaintext, 2)
    if len(ct) != len(pt):
        raise ValueError("Known plaintext and ciphertext lengths must match after filtering/padding.")
    candidates = []
    ct_nums = text_to_numbers(ct)
    pt_nums = text_to_numbers(pt)
    for key in all_invertible_2x2_keys():
        produced = []
        for i in range(0, len(pt_nums), 2):
            produced.extend(encrypt_block(pt_nums[i:i+2], key))
        if produced == ct_nums:
            candidates.append(key)
    return candidates

def key_to_matrix_str(key):
    a,b,c,d = key
    return f"[[{a:2d}, {b:2d}],\n [{c:2d}, {d:2d}]]"

# Simple usage demo if run as a script
if __name__ == "__main__":
    key = [3,3,2,5]  # example key
    plaintext = "HELLO"
    ciphertext = encrypt(plaintext, key)
    decrypted = decrypt(ciphertext, key)
    print("Example key:\n", key_to_matrix_str(key))
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted :", decrypted)

    # Demo brute-force with known plaintext/ciphertext (length 4 example)
    demo_pt = "TEST"
    demo_ct = encrypt(demo_pt, key)
    print("\nBrute-forcing key from known plaintext/ciphertext (demo)...")
    found = brute_force_known_plaintext(demo_ct, demo_pt)
    print(f"Number of candidate keys found: {len(found)}")
    if len(found) <= 20:
        for k in found:
            print(key_to_matrix_str(k))
    else:
        print("Too many results to display; first 20:")
        for k in found[:20]:
            print(key_to_matrix_str(k))
