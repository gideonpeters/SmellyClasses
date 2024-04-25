class NumericEntityUnescaper:
    def replace(self, s):
        result = ""
        i = 0
        while i < len(s):
            if s[i:i+2] == "&#":
                j = i + 2
                while j < len(s) and s[j].isdigit():
                    j += 1
                if j > i + 2:
                    num = int(s[i+2:j])
                    result += chr(num)
                    i = j
                else:
                    i += 2
            else:
                result += s[i]
                i += 1
        return result

    def is_hex_char(self, c):
        return c.isdigit() or ('A' <= c <= 'F') or ('a' <= c <= 'f')
