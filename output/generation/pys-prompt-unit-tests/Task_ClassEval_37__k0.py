class EncryptionUtils:
    def __init__(self, key):
        self.key = key

    def caesar_cipher(self, text, shift):
        if not text:
            return ""
        shifted_text = ""
        for char in text:
            if char.isalpha():
                shifted_text += chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a')).upper() if char.isupper() else chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            else:
                shifted_text += char
        return shifted_text

    def vigenere_cipher(self, text):
        if not text:
            return ""
        key_repeated = (self.key * (len(text) // len(self.key) + 1))[:len(text)]
        encrypted_text = ""
        for i in range(len(text)):
            if text[i].isalpha():
                shift = ord(key_repeated[i].lower()) - ord('a')
                encrypted_text += self.caesar_cipher(text[i], shift)
            else:
                encrypted_text += text[i]
        return encrypted_text

    def rail_fence_cipher(self, text, rails):
        if not text:
            return ""
        fence = [[] for _ in range(rails)]
        rail = 0
        direction = 1
        for char in text:
            fence[rail].append(char)
            rail += direction
            if rail == rails or rail == -1:
                direction = -direction
                rail += 2 * direction
        encrypted_text = ''.join([''.join(rail) for rail in fence])
        return encrypted_text
