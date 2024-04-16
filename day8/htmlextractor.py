import re

def extract_html_tags(html):
    pattern = r'<[^>]+>'
    html_tags = re.findall(pattern, html)
    return html_tags

# Example usage
html_string = "<div class='container'><h1>Hello, World!</h1><p>This is a sample HTML string.</p></div>"
tags = extract_html_tags(html_string)
print("HTML tags found:", tags)
