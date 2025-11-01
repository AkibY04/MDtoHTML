import re

def convert_emphasis(text: str) -> str:
    text = re.sub(r"(\*\*\*)(.*?)(\1)", r"<em><strong>\2</strong></em>", text)
    text = re.sub(r"(?<!\w)(___)(.*?)(\1)(?!\w)", r"<em><strong>\2</strong></em>", text)

    text = re.sub(r"(\*\*)(.*?)(\1)", r"<strong>\2</strong>", text)
    text = re.sub(r"(?<!\w)(__)(.*?)(\1)(?!\w)", r"<strong>\2</strong>", text)

    text = re.sub(r"(\*)(.*?)(\1)", r"<em>\2</em>", text)
    text = re.sub(r"(?<!\w)(_)(.*?)(\1)(?!\w)", r"<em>\2</em>", text)
    
    return text

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

unorderedPattern = re.compile(r"^[*\-+] (.*)$")
def convert_unordered_list(text: str) -> str:
    lines = text.split('\n')
    items = []

    for line in lines:
        match = unorderedPattern.match(line)

        if match:
            matchGroup = match.group(1)

            output = convert_code(matchGroup)
            output = convert_link(output)
            output = convert_emphasis(output)

            items.append(f"<li>{output}</li>")
    
    return f"<ul>\n" + "\n".join(items) + "\n</ul>"

convertCodePattern = re.compile(r"(``|`)(.*?)\1")
def convert_code(text: str) -> str:
    return re.sub(convertCodePattern, r"<code>\2</code>", text)

convertLinkPattern = re.compile(r"\[(.*?)\]\((.*?)\)")
def convert_link(text: str) -> str:
    return re.sub(convertLinkPattern, r'<a href="\2">\1</a>', text)

def convert(text: str) -> str:
    return

