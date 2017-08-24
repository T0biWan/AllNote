import codecs
import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension as gfm


def process_allnote(input):
    # input ist text also vielleicht immer am newline aufspalten um list zu bekommen?
    # muss am ende wieder zusammengesetzt werden damit es mit Text übereinstimmt

    input = input.split("\n")
    output = ""
    tags = []
    lines_without_markup = []
    for line in input:
        markup = get_mark_up(line)
        line_without_markup = trim_mark_up(line)
        list_items = []
        if markup.startswith("**"):
           line =  markdown.markdown("* " + line_without_markup, extensions=[gfm()])

        output += line

    return output


def get_mark_up(line):
    return line.split(" ")[0]


def trim_mark_up(line):
    return_string = ""
    for token in line.split(" ")[1:]:
        return_string += token + " "

    return return_string.rstrip()


def embed_in_html(input, title, stylesheet):
    html_begin = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n    <meta charset='UTF-8'>\n" \
                 "    <title>" + title + "</title>\n" \
                 "    <link rel='stylesheet' href='" + stylesheet + "'>\n" \
                 "</head>\n<body>\n"
    html_end = "</body>\n</html>"

    return html_begin + input + html_end


def main():
    input_file = codecs.open("input.md", mode="r", encoding="utf-8")
    output_file = codecs.open("output.html", "w", encoding="utf-8")

    input_text = input_file.read()
    title = input_file.name
    css = "css/example.css"

    output = markdown.markdown(input_text, extensions=[gfm()])
    output = embed_in_html(output, title, css)

    output_file.write(output)


#main()
a = """* list
** Sublist 1
** Sublist 1
*** Sublist 2
*** Sublist 2
** Sublist 1
* list
* list"""
print(process_allnote(a))