from md2html import *
import pytest

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
@pytest.mark.parametrize("input, output, test", [
    ("# Heading 1",                        "<h1>Heading 1</h1>",          "Normal H1 (#)"),
    ("###### Heading 6",                   "<h6>Heading 6</h6>",          "Normal H6 (######)"),
    ("Heading 1\n=======",                  "<h1>Heading 1</h1>",          "Normal H1 (alt)"),
    ("Heading 2\n---",                     "<h2>Heading 2</h2>",          "Normal H2 (alt)"),
    ("#NoSpace",                           "#NoSpace",                     "Edge case: No space"),
    ("Incorrect # Heading",                "Incorrect # Heading",          "Edge case: Not at start"),
    ("Heading 2\n-",                       "Heading 2\n-",                 "Edge case: Invalid underline"),
    ("# *Bold Heading*",                   "<h1><em>Bold Heading</em></h1>", "Integration: Emphasis"),
    ("## `Code` and [link](url)",          '<h2><code>Code</code> and <a href="url">link</a></h2>', "Integration: All inlines")
])

def test_convert_headings(input, output, test):
    assert convert_headings(input) == output

# convert_ordered_list() tests
# ======
def test_convert_ol_1(): # Normal case
    assert convert_ordered_list("1. First item\n2. Second item\n3. Third item") == "<ol>\n  <li>First item</li>\n  <li>Second item</li>\n  <li>Third item</li>\n</ol>"

def test_convert_ol_2(): # Edge case (no space after number)
    assert convert_ordered_list("1.First") == "<ol>\n\n</ol>"
# convert_unordered_list() tests
# ======
def test_convert_ul_1(): # Normal case (with *)
    assert convert_unordered_list("* Item 1\n* Item 2") == "<ul>\n  <li>Item 1</li>\n  <li>Item 2</li>\n</ul>"

def test_convert_ul_2(): # Edge case (no space after *)
    assert convert_unordered_list("*NoSpace") == "<ul>\n\n</ul>"

# convert_code() tests
# ======
def test_convert_code_1(): # Normal case (single backtick)
    assert convert_code("`Inline Code`") == "<code>Inline Code</code>"

def test_convert_code_2(): # Normal case (double backtick)
    assert convert_code("``print()``") == "<code>print()</code>"

def test_convert_code_3(): # Edge case (no backticks)
    assert convert_code("No code") == "No code"

# convert_link() tests
# ======
def test_convert_link_1(): # Normal case
    assert convert_link("[Test](https://www.test.com)") == '<a href="https://www.test.com">Test</a>'

# convert() tests
# ======
def test_convert_1(): # Normal case
    input = (
        "# Title\n\n"
        "This is a paragraph with **bold text**\n"
        "but there's also a [link](https://example.com) and `inline code`.\n\n"
        "1. First item\n"
        "2. Second item\n\n"
    )

    expected = (
        "<h1>Title</h1>\n"
        "<p>This is a paragraph with <strong>bold text</strong><br>"
        "but there's also a <a href=\"https://example.com\">link</a> and <code>inline code</code>.</p>\n"
        "<ol>\n"
        "  <li>First item</li>\n"
        "  <li>Second item</li>\n"
        "</ol>"
    )

    assert convert(input) == expected

def test_convert_2(): # Edge case (multiple newlines between paragraphs)
    md = "Paragraph 1.\n\n\n\n\n\n\n\nParagraph 2."
    expected = "<p>Paragraph 1.</p>\n<p>Paragraph 2.</p>"
    assert convert(md) == expected