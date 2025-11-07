import re
import sys

def convert_emphasis(text: str) -> str:
    text = re.sub(r"(\*\*\*)(.*?)(\1)", r"<em><strong>\2</strong></em>", text)
    text = re.sub(r"(?<!\w)(___)(.*?)(\1)(?!\w)", r"<em><strong>\2</strong></em>", text)

    text = re.sub(r"(\*\*)(.*?)(\1)", r"<strong>\2</strong>", text)
    text = re.sub(r"(?<!\w)(__)(.*?)(\1)(?!\w)", r"<strong>\2</strong>", text)

    text = re.sub(r"(\*)(.*?)(\1)", r"<em>\2</em>", text)
    text = re.sub(r"(?<!\w)(_)(.*?)(\1)(?!\w)", r"<em>\2</em>", text)
    
    return text

def convert_paragraph(text: str) -> str:
    output = convert_code(text)
    output = convert_link(output)
    output = convert_emphasis(output)

    output = output.replace('\n', '<br>')

    return f"<p>{output}</p>"

def convert_headings(text: str) -> str:
    text = re.sub(r"^(.*)\n==+", lambda m: f"<h1>{convert_emphasis(convert_link(convert_code(m.group(1))))}</h1>", text, flags=re.MULTILINE)
    text = re.sub(r"^(.*)\n--+", lambda m: f"<h2>{convert_emphasis(convert_link(convert_code(m.group(1))))}</h2>", text, flags=re.MULTILINE)

    text = re.sub(r"^###### (.*)$", lambda m: f"<h6>{convert_emphasis(convert_link(convert_code(m.group(1))))}</h6>", text, flags=re.MULTILINE)
    text = re.sub(r"^##### (.*)$", lambda m: f"<h5>{convert_emphasis(convert_link(convert_code(m.group(1))))}</h5>", text, flags=re.MULTILINE)
    text = re.sub(r"^#### (.*)$", lambda m: f"<h4>{convert_emphasis(convert_link(convert_code(m.group(1))))}</h4>", text, flags=re.MULTILINE)
    text = re.sub(r"^### (.*)$", lambda m: f"<h3>{convert_emphasis(convert_link(convert_code(m.group(1))))}</h3>", text, flags=re.MULTILINE)
    text = re.sub(r"^## (.*)$", lambda m: f"<h2>{convert_emphasis(convert_link(convert_code(m.group(1))))}</h2>", text, flags=re.MULTILINE)
    text = re.sub(r"^# (.*)$", lambda m: f"<h1>{convert_emphasis(convert_link(convert_code(m.group(1))))}</h1>", text, flags=re.MULTILINE)

    return text

orderedPattern = re.compile(r"^[0-9]+\. (.*)$")
def convert_ordered_list(text: str) -> str:
    lines = text.split('\n')
    items = []

    for line in lines:
        match = orderedPattern.match(line)

        if match:
            matchGroup = match.group(1)

            output = convert_code(matchGroup)
            output = convert_link(output)
            output = convert_emphasis(output)

            items.append(f"  <li>{output}</li>")
    
    return f"<ol>\n" + "\n".join(items) + "\n</ol>"

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

            items.append(f"  <li>{output}</li>")
    
    return f"<ul>\n" + "\n".join(items) + "\n</ul>"

convertCodePattern = re.compile(r"(``|`)(.*?)\1")
def convert_code(text: str) -> str:
    return re.sub(convertCodePattern, r"<code>\2</code>", text)

convertLinkPattern = re.compile(r"\[(.*?)\]\((.*?)\)")
def convert_link(text: str) -> str:
    return re.sub(convertLinkPattern, r'<a href="\2">\1</a>', text)

def convert(text: str) -> str:
    blocks = re.split(r'\n\n+', text.strip())
    htmlArr = []
    
    for block in blocks:
        block = block.strip()
        
        converted_heading = convert_headings(block)
        if converted_heading != block:
            htmlArr.append(converted_heading)
            continue

        firstLine = block.split('\n')[0]
        if unorderedPattern.match(firstLine):
            htmlArr.append(convert_unordered_list(block))
        elif orderedPattern.match(firstLine):
            htmlArr.append(convert_ordered_list(block))
        else:
            htmlArr.append(convert_paragraph(block))
            
    return "\n".join(htmlArr)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        inputFile = sys.argv[1]
        if not inputFile.endswith('.md'):
            print("Input file must have a .md extension.")
            sys.exit(1)

    if len(sys.argv) == 3:
        outputFile = sys.argv[2]
    elif len(sys.argv) == 2:
        if inputFile.endswith('.md'):
            outputFile = inputFile[:-3] + '.html'
        else:
            outputFile = inputFile + '.html'
    else:
        print("Incorrect input. Correct usage: python md2html.py input.md [output.html]")
        sys.exit(1)

    try:
        with open(inputFile, 'r') as f:
            md = f.read()
            
        html = convert(md)

        with open(outputFile, 'w') as f:
            f.write(html)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)