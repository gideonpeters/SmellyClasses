import re

class HtmlUtil:
    @staticmethod
    def __format_line_feed(text):
        return re.sub(r'\n{2,}', '\n', text)

    def format_line_html_text(self, html_text):
        code_blocks = re.findall(r'<pre><code>(.*?)</code></pre>', html_text, re.DOTALL)
        formatted_text = re.sub(r'<.*?>', '', html_text)
        for code_block in code_blocks:
            formatted_text = formatted_text.replace(f'<pre><code>{code_block}</code></pre>', '-CODE-')
        return formatted_text.strip()

    def extract_code_from_html_text(self, html_text):
        return re.findall(r'<pre><code>(.*?)</code></pre>', html_text, re.DOTALL)
