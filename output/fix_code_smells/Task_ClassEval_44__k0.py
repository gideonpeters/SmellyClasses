import re

class HtmlUtil:
    CODE_MARK = '-CODE-'

    def format_line_html_text(self, html_text):
        title = re.search(r'<h1>(.*?)</h1>', html_text, re.DOTALL)
        paragraphs = re.findall(r'<p>(.*?)</p>', html_text, re.DOTALL)
        codes = re.findall(r'<pre><code>(.*?)</code></pre>', html_text, re.DOTALL)
        
        result = ''
        if title:
            result += title.group(1) + '\n'
        for paragraph in paragraphs:
            result += paragraph + '\n'
        for code in codes:
            result += self.CODE_MARK + '\n'
        
        return result

    def extract_code_from_html_text(self, html_text):
        codes = re.findall(r'<pre><code>(.*?)</code></pre>', html_text, re.DOTALL)
        return codes if codes else []

if __name__ == '__main__':
    unittest.main()