class DecryptionUtils:
    """
    This is a class that provides methods for decryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption, str.
        """
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        """
        Deciphers the given ciphertext using the Caesar cipher
        :param ciphertext: The ciphertext to decipher, str.
        :param shift: The shift to use for decryption, int.
        :return: The deciphered plaintext, str.
        """
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                decrypted_text += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                decrypted_text += char
        return decrypted_text

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher, str.
        :return: The deciphered plaintext, str.
        """
        decrypted_text = ""
        key_length = len(self.key)
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                shift = ord(self.key[key_index % key_length].lower()) - ord('a')
                decrypted_text += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher, str.
        :param rails: The number of rails to use for decryption, int.
        :return: The deciphered plaintext, str.
        """
        rail_fence = ['' for _ in range(rails)]
        direction = -1
        row = 0
        for char in encrypted_text:
            rail_fence[row] += char
            if row == 0 or row == rails - 1:
                direction *= -1
            row += direction
        decrypted_text = ''.join(rail_fence)
        return decrypted_text
