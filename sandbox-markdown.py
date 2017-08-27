import re
import codecs
import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension as gfm

allnote_tags = {"inline-code": "§", "multiline-code": "§§"}
markdown_tags = {"inline-code": "`", "multiline-code": "```"}
html_tags = {}
regex = {"is-inline-code": r"" + allnote_tags["inline-code"] + "(.+)" + allnote_tags["inline-code"],
         "process-inline-code": r"(" + allnote_tags["inline-code"] + "([^" + allnote_tags["inline-code"] + "]+)" + allnote_tags["inline-code"] + ")+",
         "is-multiline-code": r"" + allnote_tags["multiline-code"]}


# Todo überarbeiten
def process_allnote(input):
    output = ""
    input_line_by_line = input.split("\n")
    for line in input_line_by_line:
        markup = get_mark_up(line)
        line_without_markup = trim_mark_up(line)
        if is_inline_code(line):
            line = process_inline_code(line)
        if is_multiline_code(line):
            line = process_multiline_code(line)
        if is_ordered_list(line):
            line = process_ordered_list(line)

        output += line + "\n"

    return output


# Todo überarbeiten
def process_sublist(input):
    output = ""
    input_line_by_line = input.split("\n")
    list_level_current = 0
    list_level_line = 0
    for line in input_line_by_line:
        markup = get_mark_up(line)
        line_without_markup = trim_mark_up(line)
        if is_unordered_list(line):
            list_level_line = len(markup)
            if list_level_current == list_level_line:
                if list_level_line > 1:
                    line = "<li>" + line_without_markup + "</li>"
            elif is_sublist(list_level_current, list_level_line):
                if list_level_line > 1:
                    line = "\n<ul>\n" + "<li>" + line_without_markup + "</li>"
            elif is_superlist(list_level_current, list_level_line):
                line = "</ul>\n"
                if list_level_line > 1:
                    line += "<li>" + line_without_markup + "</li>"
                else:
                    line += markup + " " + line_without_markup
            list_level_current = list_level_line
        output += line + "\n"

    return output


# Todo überarbeiten
def process_ordered_list(line):
    markup = get_mark_up(line)
    line_without_markup = trim_mark_up(line)
    line = "1. " + line_without_markup
    return line + "\n"


def process_inline_code(line):
    pattern = regex["process-inline-code"]
    replace = r""+markdown_tags["inline-code"]+"\2"+markdown_tags["inline-code"]
    line = re.sub(pattern, replace, line)
    return line


def process_multiline_code(line):
    pattern = regex["is-multiline-code"]
    replace = r""+markdown_tags["multiline-code"]
    line = re.sub(pattern, replace, line)
    return line


# Todo überarbeiten
def is_ordered_list(line):
    return line.startswith("+")


# Todo überarbeiten
def is_unordered_list(line):
    return line.startswith("*")


def is_multiline_code(line):
    pattern = regex["is-multiline-code"]
    return True if re.search(pattern, line) else False


def is_inline_code(line):
    pattern = regex["is-inline-code"]
    return True if re.search(pattern, line) else False


# Todo überarbeiten
def is_sublist(list_level_current, list_level_line):
    return list_level_current < list_level_line


# Todo überarbeiten
def is_superlist(list_level_current, list_level_line):
    return list_level_current > list_level_line


def get_mark_up(line):
    return line.split(" ")[0]


def trim_mark_up(line):
    return_string = ""
    for token in line.split(" ")[1:]:
        return_string += token + " "

    return return_string.rstrip()


# Todo überarbeiten
def embed_in_html(input, title, stylesheet):
    html_begin = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n    <meta charset='UTF-8'>\n" \
                 "    <title>" + title + "</title>\n" \
                                         "    <link rel='stylesheet' href='" + stylesheet + "'>\n" \
                                                                                            "</head>\n<body>\n"
    html_end = "</body>\n</html>"

    return html_begin + input + html_end


# Todo überarbeiten
def main():
    input_file = codecs.open("input1.md", mode="r", encoding="utf-8")
    output_file = codecs.open("output.html", "w", encoding="utf-8")

    input_text = input_file.read()
    title = input_file.name
    css = "css/example.css"

    output = process_allnote(input_text)

    output = markdown.markdown(output, extensions=[gfm()])
    output = embed_in_html(output, title, css)

    output_file.write(output)


main()
