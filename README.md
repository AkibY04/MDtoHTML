# Markdown to HTML Converter | CSE 337 Assignment 2
## Limitations
As according to the assignment document, the script follows the following limitations:
- Block elements like headings, lists, and paragraphs are separated by at least one blank line, signified by `\n\n` in markdown
- Both ordered and unordered lists have a two space indent for each list item
- Lists can't have other lists or block elements
- Only markdown features mentioned in the assignment are supported. Features like multi-line code blocks aren't supported
## Running tests with pytest
test_md2html.py contains test cases that can be ran via pytest. In order to run the test cases:
1. Ensure that conda is installed. Running `conda --version` should output a version number. Otherwise, you should install a version of Conda such as Miniconda.
2. Create an isolated Python environment from the given `environment.yml` file by running `conda env create -f environment.yml`. This will create an environment called `md2html-env`.
3. Activate the environment with `conda activate md2html-env`
4. Run the tests with `pytest`