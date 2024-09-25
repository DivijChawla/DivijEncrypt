# DivijEncrypt

**DivijEncrypt** is a Python library that provides multiple encryption techniques, ranging from simple shuffling to more complex mathematical and matrix-based encryption methods. The library is designed for educational purposes and experimentation with various encryption algorithms.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Encryption Methods](#encryption-methods)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

DivijEncrypt provides the following encryption techniques:
- **Shuffle-Key Encryption**: Randomly shuffles the text using a key.
- **Color Matrix Substitution**: Substitutes characters with colors.
- **Decimal Swapping**: Swaps the ASCII values of adjacent characters.
- **Layered Modulus Cipher**: Encrypts using modular arithmetic.
- **Clockwise Spiral Encoding**: Encrypts text in a spiral pattern.
- **Linked Word Encryption**: Encrypts based on the length of previous words.
- **Symbolic Chessboard Encryption**: Uses knight moves on a chessboard to encode text.
- **Prime Product Scrambling**: Multiplies character values by prime numbers.
- **Palindromic Padding**: Creates a palindromic string.
- **Coordinate Map Encryption**: Treats characters as coordinates on a grid.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DivijEncrypt.git
   cd DivijEncrypt
   ```

2. Install the necessary dependencies:
   ```bash
   pip install numpy
   ```

3. Ensure that you're using **Python 3.x** to run the library.

## Usage

To use DivijEncrypt, import the necessary functions from the module. Each encryption method has both an encryption and a decryption function. Here is a basic example of how to use the library:

```python
from DivijEncrypt import layered_modulus_encrypt, layered_modulus_decrypt

plaintext = "HELLO WORLD"
key = 7  # The encryption key, must be coprime with 255

# Encryption
encrypted = layered_modulus_encrypt(plaintext, key)
print(f"Encrypted text: {encrypted}")

# Decryption
decrypted = layered_modulus_decrypt(encrypted, key)
print(f"Decrypted text: {decrypted}")
```

## Encryption Methods

Below are brief descriptions of each encryption method:

1. **Shuffle-Key Encryption**: Uses a random key to shuffle the characters of a string.
2. **Color Matrix Substitution**: Maps each character to a randomly generated color in hexadecimal format.
3. **Decimal Swapping**: Swaps adjacent ASCII character codes.
4. **Layered Modulus Cipher**: Encrypts text using modular arithmetic, provided the key is coprime with 255.
5. **Clockwise Spiral Encoding**: Fills a matrix with characters and reads them in a spiral pattern.
6. **Linked Word Encryption**: Encrypts words based on the length of the previous word.
7. **Symbolic Chessboard Encryption**: Encrypts text by simulating knight moves on a chessboard.
8. **Prime Product Scrambling**: Uses multiplication by prime numbers to scramble text.
9. **Palindromic Padding**: Creates a palindrome by appending the reverse of the original text.
10. **Coordinate Map Encryption**: Shifts characters using a grid coordinate system.

## Examples

Here are some examples of the various encryption techniques:

### 1. Shuffle-Key Encryption

```python
from DivijEncrypt import generate_key, shuffle_encrypt, shuffle_decrypt

text = "HELLO"
key = generate_key(len(text))

# Encryption
encrypted = shuffle_encrypt(text, key)

# Decryption
decrypted = shuffle_decrypt(encrypted, key)
```

### 2. Color Matrix Substitution

```python
from DivijEncrypt import color_matrix_encrypt, color_matrix_decrypt

text = "HELLO"
encrypted = color_matrix_encrypt(text)
decrypted = color_matrix_decrypt(encrypted)
```

### 3. Layered Modulus Cipher

```python
from DivijEncrypt import layered_modulus_encrypt, layered_modulus_decrypt

text = "HELLO"
key = 7

encrypted = layered_modulus_encrypt(text, key)
decrypted = layered_modulus_decrypt(encrypted, key)
```

### 4. Palindromic Padding

```python
from DivijEncrypt import palindromic_padding_encrypt, palindromic_padding_decrypt

text = "HELLO"
encrypted = palindromic_padding_encrypt(text)
decrypted = palindromic_padding_decrypt(encrypted)
```

### 5. Coordinate Map Encryption

```python
from DivijEncrypt import coordinate_map_encrypt, coordinate_map_decrypt

text = "HELLO"
encrypted = coordinate_map_encrypt(text)
decrypted = coordinate_map_decrypt(encrypted)
```

## Contributing

Contributions are welcome! If you have new encryption methods, improvements, or bug fixes, feel free to fork the repository and submit a pull request.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature-or-bugfix-branch
   ```
3. Commit your changes and push to the new branch:
   ```bash
   git commit -m "Description of feature or bug fix"
   git push origin feature-or-bugfix-branch
   ```
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

