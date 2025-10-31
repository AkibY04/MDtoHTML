import re

def convert_emphasis(text: str) -> str:
    return

def convert_paragraph(text: str) -> str:
    return

def convert_headings(text: str) -> str:
    text = re.sub(r"^(.*)\n==+", r"<h1>\1</h1>", text, flags=re.MULTILINE)
    text = re.sub(r"^(.*)\n--+", r"<h2>\1</h2>", text, flags=re.MULTILINE)

    text = re.sub(r"^###### (.*)$", r"<h6>\1</h6>", text, flags=re.MULTILINE)
    text = re.sub(r"^##### (.*)$", r"<h5>\1</h5>", text, flags=re.MULTILINE)
    text = re.sub(r"^#### (.*)$", r"<h4>\1</h4>", text, flags=re.MULTILINE)
    text = re.sub(r"^### (.*)$", r"<h3>\1</h3>", text, flags=re.MULTILINE)
    text = re.sub(r"^## (.*)$", r"<h2>\1</h2>", text, flags=re.MULTILINE)
    text = re.sub(r"^# (.*)$", r"<h1>\1</h1>", text, flags=re.MULTILINE)

    return text

def convert_ordered_list(text: str) -> str:
    return

def convert_unordered_list(text: str) -> str:
    return

def convert_code(text: str) -> str:
    pattern = r"(``|`)(.*?)\1"
    output = r"<code>\2</code>"
    
    return re.sub(pattern, output, text)

def convert_link(text: str) -> str:
    pattern = r"\[(.*?)\]\((.*?)\)"
    output = r'<a href="\2">\1</a>'
    
    return re.sub(pattern, output, text)

def convert(text: str) -> str:
    return

