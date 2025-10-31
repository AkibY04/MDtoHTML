from md2html import *

# convert_emphasis() tests
# ======

# convert_paragraph() tests
# ======

# convert_headings() tests
# ======
def test_convert_heading_1(): # Normal case (H1 with #)
    assert convert_headings("# Heading 1") == "<h1>Heading 1</h1>"

def test_convert_heading_2(): # Normal case (H6)
    assert convert_headings("###### Heading 6") == "<h6>Heading 6</h6>"

def test_convert_heading_3(): # Normal case (H1 with ==)
    assert convert_headings("Heading 1\n=======") == "<h1>Heading 1</h1>"

def test_convert_heading_4(): # Normal case (H2 with --)
    assert convert_headings("Heading 2\n---") == "<h2>Heading 2</h2>"

def test_convert_heading_5(): # Edge case (No space after #)
    assert convert_headings("#Nothing") == "#Nothing"

def test_convert_heading_6(): # Edge case (Not at start of line)
    text = "Incorrect # Heading"

    assert convert_headings(text) == text

def test_convert_heading_7(): # Edge case (Invalid underline for H2)
    text = "Heading 2\n-"

    assert convert_headings(text) == text

# convert_ordered_list() tests
# ======

# convert_unordered_list() tests
# ======

# convert_code() tests
# ======
def test_convert_code_1(): #Normal case (single backtick)
    assert convert_code("`Inline Code`") == "<code>Inline Code</code>"

def test_convert_code_2(): #Normal case (double backtick)
    assert convert_code("``print()``") == "<code>print()</code>"

def test_convert_code_3(): #Edge case (no backticks)
    assert convert_code("No code") == "No code"

# convert_link() tests
# ======
def test_convert_link_1(): # Normal case
    assert convert_link("[Test](https://www.test.com)") == '<a href="https://www.test.com">Test</a>'

# convert() tests
# ======