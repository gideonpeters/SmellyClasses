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
        for i in range(len(self.pattern)):
            if self.pattern[i] not in bad_chars:
                bad_chars.append(self.pattern[i])
        return [self.pattern.index(char) for char in bad_chars]

if __name__ == '__main__':
    import unittest

    class BoyerMooreSearchTestMatchInPattern(unittest.TestCase):
        def test_match_in_pattern(self):
            boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
            self.assertEqual(boyerMooreSearch.match_in_pattern("A"), 0)

        def test_match_in_pattern_2(self):
            boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABAB")
            self.assertEqual(boyerMooreSearch.match_in_pattern("B"), 3)

        def test_match_in_pattern_3(self):
            boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABCABC")
            self.assertEqual(boyerMooreSearch.match_in_pattern("C"), 5)

        def test_match_in_pattern_4(self):
            boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABCABC")
            self.assertEqual(boyerMooreSearch.match_in_pattern("D"), -1)

        def test_match_in_pattern_5(self):
            boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABCABC")
            self.assertEqual(boyerMooreSearch.match_in_pattern("E"), -1)

    class BoyerMooreSearchTestMismatchInText(unittest.TestCase):
        def test_mismatch_in_text(self):
            boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
            self.assertEqual(boyerMooreSearch.mismatch_in_text(0), -1)

        def test_mismatch_in_text_2(self):
            boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
            self.assertEqual(boyerMooreSearch.mismatch_in_text(0), 2)

        def test_mismatch_in_text_3(self):
            boyerMooreSearch = BoyerMooreSearch("AAAA", "ABC")
            self.assertEqual(boyerMooreSearch.mismatch_in_text(0), 2)

        def test_mismatch_in_text_4(self):
            boyerMooreSearch = BoyerMooreSearch("ABAABA", "")
            self.assertEqual(boyerMooreSearch.mismatch_in_text(0), -1)

        def test_mismatch_in_text_5(self):
            boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
            self.assertEqual(boyerMooreSearch.mismatch_in_text(3), 5)

    class BoyerMooreSearchTestBadCharacterHeuristic(unittest.TestCase):
        def test_bad_character_heuristic(self):
            boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
            self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [0, 3])

        def test_bad_character_heuristic_2(self):
            boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
            self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [])

        def test_bad_character_heuristic_3(self):
            boyerMooreSearch = BoyerMooreSearch("ABAABA", "")
            self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [0, 1, 2, 3, 4, 5, 6])

        def test_bad_character_heuristic_4(self):
            boyerMooreSearch = BoyerMooreSearch("ABACABA", "ABA")
            self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [0, 4])

        def test_bad_character_heuristic_5(self):
            boyerMooreSearch = BoyerMooreSearch("ABACABA", "ABAC")
            self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [0])

    class BoyerMooreSearchTestMain(unittest.TestCase):
        def test_main(self):
            boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
            self.assertEqual(boyerMooreSearch.match_in_pattern("A"), 0)
            self.assertEqual(boyerMooreSearch.mismatch_in_text(0), -1)
            self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [0, 3])

    unittest.main()
