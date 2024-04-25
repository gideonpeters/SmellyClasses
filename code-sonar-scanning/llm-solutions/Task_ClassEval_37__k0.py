class EncryptionUtils:
    def __init__(self, key):
        self.key = key

    def caesar_cipher(self, text, shift):
        if not text:
            return ""
        shifted_text = ""
        for char in text:
            if char.isalpha():
                shift_amount = (ord(char.lower()) - ord('a') + shift) % 26
                shifted_char = chr(ord('a') + shift_amount) if char.islower() else chr(ord('A') + shift_amount)
                shifted_text += shifted_char
            else:
                shifted_text += char
        return shifted_text

    def vigenere_cipher(self, text):
        if not text:
            return ""
        key_length = len(self.key)
        encrypted_text = ""
        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(self.key[i % key_length].lower()) - ord('a')
                shift_amount = (ord(char.lower()) - ord('a') + shift) % 26
                shifted_char = chr(ord('a') + shift_amount) if char.islower() else chr(ord('A') + shift_amount)
                encrypted_text += shifted_char
            else:
                encrypted_text += char
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
