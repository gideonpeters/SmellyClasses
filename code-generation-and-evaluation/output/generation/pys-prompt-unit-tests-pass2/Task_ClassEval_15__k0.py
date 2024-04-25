class BoyerMooreSearch:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern

    def match_in_pattern(self, char):
        if char in self.pattern:
            return self.pattern.index(char)
        else:
            return -1

    def mismatch_in_text(self, index):
        if index < len(self.text):
            if self.text[index] not in self.pattern:
                return index
            else:
                return -1
        else:
            return -1

    def bad_character_heuristic(self):
        bad_chars = []
        for i in range(len(self.text) - len(self.pattern) + 1):
            if self.text[i:i+len(self.pattern)] != self.pattern:
                bad_chars.append(i)
        return bad_chars
