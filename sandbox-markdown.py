import codecs
import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension as gfm


def process_allnote(input):
    pass


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


def is_unordered_list(line):
    return line.startswith("*")


def is_sublist(list_level_current, list_level_line):
    return list_level_current < list_level_line


def is_superlist(list_level_current, list_level_line):
    return list_level_current > list_level_line


def get_mark_up(line):
    return line.split(" ")[0]


def trim_mark_up(line):
    return_string = ""
    for token in line.split(" ")[1:]:
        return_string += token + " "

    return return_string.rstrip()


def line_has_markup(line):
    return get_mark_up(line) in allnote


def embed_in_html(input, title, stylesheet):
    html_begin = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n    <meta charset='UTF-8'>\n" \
                 "    <title>" + title + "</title>\n" \
                                         "    <link rel='stylesheet' href='" + stylesheet + "'>\n" \
                                                                                            "</head>\n<body>\n"
    html_end = "</body>\n</html>"

    return html_begin + input + html_end


def main():
    input_file = codecs.open("input1.md", mode="r", encoding="utf-8")
    output_file = codecs.open("output.html", "w", encoding="utf-8")

    input_text = input_file.read()
    title = input_file.name
    css = "css/example.css"

    input_text = process_sublist(input_text)

    output = markdown.markdown(input_text, extensions=[gfm()])
    output = embed_in_html(output, title, css)

    output_file.write(output)


main()
