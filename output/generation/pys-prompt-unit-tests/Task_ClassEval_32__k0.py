class DecryptionUtils:
    def __init__(self, key):
        self.key = key

    def caesar_decipher(self, text, shift):
        result = ''
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                result += decrypted_char
            else:
                result += char
        return result

    def vigenere_decipher(self, text):
        result = ''
        key_index = 0
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                shift = ord(self.key[key_index % len(self.key)]) - ascii_offset
                decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                result += decrypted_char
                key_index += 1
            else:
                result += char
        return result

    def rail_fence_decipher(self, text, rails):
        result = [''] * len(text)
        index = 0
        for i in range(rails):
            step1 = (rails - i - 1) * 2
            step2 = i * 2
            pos = i
            while pos < len(text):
                if step1 != 0:
                    result[pos] = text[index]
                    index += 1
                    pos += step1
                if pos < len(text) and step2 != 0:
                    result[pos] = text[index]
                    index += 1
                    pos += step2
        return ''.join(result)
