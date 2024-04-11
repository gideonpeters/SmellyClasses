class Manacher:
    PALINDROMIC_PATTERN = 'a|b|a|b|a'

    def __init__(self, s):
        self.s = s
        self.p = [0] * (2 * len(s) + 1)
        self.s_new = ['#'] * (2 * len(s) + 1)
        for i in range(len(s)):
            self.s_new[2 * i + 1] = s[i]
        self.s_new = ''.join(self.s_new)
        self.palindromic_length(2, 1)

    def palindromic_length(self, center, radius):
        while self.s_new[center - radius] == self.s_new[center + radius]:
            radius += 1
        return radius - 1

    def palindromic_string(self):
        max_len = 0
        start = 0
        for i in range(len(self.p)):
            if self.p[i] > max_len:
                max_len = self.p[i]
                start = i
        return self.s[(start - max_len) // 2: (start + max_len) // 2]

if __name__ == '__main__':
    import unittest

    class ManacherTestPalindromicLength(unittest.TestCase):
        def test_palindromic_length(self):
            manacher = Manacher('ababa')
            self.assertEqual(manacher.palindromic_length(2, 1), 2)

        def test_palindromic_length_2(self):
            manacher = Manacher('ababaxse')
            self.assertEqual(manacher.palindromic_length(2, 1), 2)

        def test_palindromic_length_3(self):
            manacher = Manacher('ababax')
            self.assertEqual(manacher.palindromic_length(2, 3), 0)

        def test_palindromic_length_4(self):
            manacher = Manacher('ababax')
            self.assertEqual(manacher.palindromic_length(9, 2), 0)

        def test_palindromic_length_5(self):
            manacher = Manacher('ababax')
            self.assertEqual(manacher.palindromic_length(4, 1), 4)

    class ManacherTestPalindromicString(unittest.TestCase):
        def test_palindromic_string(self):
            manacher = Manacher('ababaxse')
            self.assertEqual(manacher.palindromic_string(), 'ababa')

        def test_palindromic_string_2(self):
            manacher = Manacher('ababax')
            self.assertEqual(manacher.palindromic_string(), 'ababa')

        def test_palindromic_string_3(self):
            manacher = Manacher('ababax')
            self.assertEqual(manacher.palindromic_string(), 'ababa')

        def test_palindromic_string_4(self):
            manacher = Manacher('ababaxssss')
            self.assertEqual(manacher.palindromic_string(), 'ababa')

        def test_palindromic_string_5(self):
            manacher = Manacher('abab')
            self.assertEqual(manacher.palindromic_string(), 'aba')

    class ManacherTestMain(unittest.TestCase):
        def test_main(self):
            manacher = Manacher('ababa')
            self.assertEqual(manacher.palindromic_length(2, 1), 2)
            self.assertEqual(manacher.palindromic_string(), 'ababa')

    unittest.main()