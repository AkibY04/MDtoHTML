from md2html import *

# convert_emphasis() tests
# ======
def test_convert_emphasis_1(): # Normal case (double asteriks)
    assert convert_emphasis("all that glitters is **not** gold") == "all that glitters is <strong>not</strong> gold"

def test_convert_emphasis_2(): # Normal case (double underscore + single underscore)
    assert convert_emphasis("This text is ___really important___.") == "This text is <em><strong>really important</strong></em>."

def test_convert_emphasis_3(): # Edge case (invalid emphasis)
    assert convert_emphasis("all that g__litters__ is not g__o__ld") == "all that g__litters__ is not g__o__ld"

# convert_paragraph() tests
# ======
def test_convert_paragraph_1(): # Normal case
    assert (convert_paragraph("This is a single line.\nIt is the first paragraph in this example.") == "<p>This is a single line.<br>It is the first paragraph in this example.</p>")



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
    assert convert_headings("Incorrect # Heading") == "Incorrect # Heading"

def test_convert_heading_7(): # Edge case (Invalid underline for H2)
    assert convert_headings("Heading 2\n-") == "Heading 2\n-"

# convert_ordered_list() tests
# ======
def test_convert_ol_1(): # Normal case
    assert convert_ordered_list("1. First item\n2. Second item\n3. Third item") == "<ol>\n<li>First item</li>\n<li>Second item</li>\n<li>Third item</li>\n</ol>"

def test_convert_ol_2(): # Edge case (no space after number)
    assert convert_ordered_list("1.First") == "<ol>\n\n</ol>"
# convert_unordered_list() tests
# ======
def test_convert_ul_1(): # Normal case (with *)
    assert convert_unordered_list("* Item 1\n* Item 2") == "<ul>\n<li>Item 1</li>\n<li>Item 2</li>\n</ul>"

def test_convert_ul_2(): # Edge case (no space after *)
    assert convert_unordered_list("*NoSpace") == "<ul>\n\n</ul>"

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