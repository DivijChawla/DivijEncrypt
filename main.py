import random
import string
import numpy as np
import math

# Helper function to generate a random key for shuffle
def generate_key(length):
    return random.sample(range(length), length)

# Method 1: Shuffle-Key Encryption
def shuffle_encrypt(text, key):
    shuffled = ''.join([text[i] for i in key])
    return shuffled

def shuffle_decrypt(text, key):
    unshuffled = [''] * len(text)
    for i, val in enumerate(key):
        unshuffled[val] = text[i]
    return ''.join(unshuffled)

# Method 2: Color Matrix Substitution
color_map = {char: f'#{random.randint(0, 0xFFFFFF):06x}' for char in string.printable}
reverse_color_map = {v: k for k, v in color_map.items()}

def color_matrix_encrypt(text):
    return ''.join([color_map[char] for char in text])

def color_matrix_decrypt(text):
    return ''.join([reverse_color_map[text[i:i+7]] for i in range(0, len(text), 7)])

# Method 3: Decimal Swapping
def decimal_swap_encrypt(text):
    codes = [ord(c) for c in text]
    swapped = []
    for i in range(0, len(codes), 2):
        if i + 1 < len(codes):
            swapped.extend([codes[i+1], codes[i]])
        else:
            swapped.append(codes[i])
    return ''.join(chr(c) for c in swapped)

def decimal_swap_decrypt(text):
    codes = [ord(c) for c in text]
    swapped = []
    for i in range(0, len(codes), 2):
        if i + 1 < len(codes):
            swapped.extend([codes[i+1], codes[i]])
        else:
            swapped.append(codes[i])
    return ''.join(chr(c) for c in swapped)

# Helper function to check if a key is valid (i.e., coprime with the modulus)
def is_key_valid(key, modulus=255):
    return math.gcd(key, modulus) == 1

# Method 4: Layered Modulus Cipher with key check
def layered_modulus_encrypt(text, key):
    if not is_key_valid(key):
        raise ValueError(f"Key {key} is not valid (must be coprime with 255)")
    return ''.join([chr((ord(c) * key) % 255) for c in text])

def layered_modulus_decrypt(text, key):
    if not is_key_valid(key):
        raise ValueError(f"Key {key} is not valid (must be coprime with 255)")
    key_inverse = pow(key, -1, 255)  # Inverse key under mod 255
    return ''.join([chr((ord(c) * key_inverse) % 255) for c in text])

# Method 5: Clockwise Spiral Encoding
def spiral_encrypt(text, size):
    grid = np.array(list(text.ljust(size**2)))[:size**2].reshape((size, size))
    spiral_order = []
    while grid.size:
        spiral_order.extend(grid[0])  # Top row
        grid = grid[1:].T[::-1]  # Rotate
    return ''.join(spiral_order)

def spiral_decrypt(text, size):
    grid = np.empty((size, size), dtype=str)
    idx = 0
    layers = []
    while idx < len(text):
        layers.append(list(text[idx:idx + size]))
        idx += size
    return ''.join(np.concatenate(layers).ravel())

# Method 6: Linked Word Encryption
def linked_word_encrypt(text):
    words = text.split(' ')
    encrypted_words = []
    prev_len = len(words[0])
    for i, word in enumerate(words):
        shift = prev_len
        encrypted_word = ''.join([chr(((ord(c) - 32 + shift) % 95) + 32) for c in word])
        encrypted_words.append(encrypted_word)
        prev_len = len(word)
    return ' '.join(encrypted_words)

def linked_word_decrypt(text):
    words = text.split(' ')
    decrypted_words = []
    prev_len = len(words[0])
    for i, word in enumerate(words):
        shift = prev_len
        decrypted_word = ''.join([chr(((ord(c) - 32 - shift) % 95) + 32) for c in word])
        decrypted_words.append(decrypted_word)
        prev_len = len(word)
    return ' '.join(decrypted_words)

# Method 7: Symbolic Chessboard Encryption (extended to handle more characters)
# Expanding the chessboard to handle more characters, not just A-H
valid_chars = string.ascii_uppercase + string.digits + string.punctuation + ' '
chessboard_size = 8
chessboard = [[valid_chars[i + j * chessboard_size] for i in range(chessboard_size)] for j in range(chessboard_size)]
chess_pos = {chessboard[r][c]: (r, c) for r in range(chessboard_size) for c in range(chessboard_size)}

def chessboard_encrypt(text):
    encrypted = []
    for char in text.upper():
        if char in chess_pos:
            r, c = chess_pos[char]
            new_r, new_c = (r + 1) % chessboard_size, (c + 2) % chessboard_size  # Simulating a knight move
            encrypted.append(chessboard[new_r][new_c])
        else:
            encrypted.append(char)  # If character is not on the chessboard, keep it unchanged
    return ''.join(encrypted)

def chessboard_decrypt(text):
    decrypted = []
    for char in text.upper():
        if char in chess_pos:
            r, c = chess_pos[char]
            new_r, new_c = (r - 1) % chessboard_size, (c - 2) % chessboard_size  # Reverse knight move
            decrypted.append(chessboard[new_r][new_c])
        else:
            decrypted.append(char)  # If character is not on the chessboard, keep it unchanged
    return ''.join(decrypted)

# Method 8: Prime Product Scrambling
def prime_product_encrypt(text, prime):
    return ''.join([chr((ord(c) * prime) % 255) for c in text])

def prime_product_decrypt(text, prime):
    return ''.join([chr((ord(c) * pow(prime, -1, 255)) % 255) for c in text])

# Method 9: Palindromic Padding
def palindromic_padding_encrypt(text):
    return text + text[::-1]

def palindromic_padding_decrypt(text):
    half = len(text) // 2
    return text[:half]

# Method 10: Coordinate Map Encryption
def coordinate_map_encrypt(text):
    coords = [(ord(c) % 16, ord(c) // 16) for c in text]
    shifted = [(x + 1, y + 2) for x, y in coords]  # Shift coordinates
    return ''.join([chr(x + y * 16) for x, y in shifted])

def coordinate_map_decrypt(text):
    coords = [(ord(c) % 16, ord(c) // 16) for c in text]
    shifted = [(x - 1, y - 2) for x, y in coords]
    return ''.join([chr(x + y * 16) for x, y in shifted])

# Example of encryption and decryption
plaintext = "HELLO WORLD"
key = 7  # Valid key (coprime with 255)

encrypted = layered_modulus_encrypt(plaintext, key)
print("Encrypted:", encrypted)

decrypted = layered_modulus_decrypt(encrypted, key)
print("Decrypted:", decrypted)
