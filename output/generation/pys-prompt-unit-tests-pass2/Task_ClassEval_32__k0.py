class DecryptionUtils:
    def __init__(self, key):
        self.key = key

    def caesar_decipher(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                result += decrypted_char
            else:
                result += char
        return result

    def vigenere_decipher(self, text):
        result = ""
        key_len = len(self.key)
        key_index = 0
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                shift = ord(self.key[key_index % key_len].lower()) - 97
                decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                result += decrypted_char
                key_index += 1
            else:
                result += char
        return result

    def rail_fence_decipher(self, text, rails):
        result = [''] * rails
        current_rail = 0
        direction = 1
        for char in text:
            result[current_rail] += char
            current_rail += direction
            if current_rail == rails - 1 or current_rail == 0:
                direction *= -1
        return ''.join(result)

if __name__ == '__main__':
    unittest.main()
