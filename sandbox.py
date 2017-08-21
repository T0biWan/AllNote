import logging
import sys

# create and configure logger
LOG_FORMAT = '%(levelname)s:%(funcName)s:%(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, filemode='w', format=LOG_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

allnote_html = {"#": ["<h1>", "</h1>"], "##": ["<h2>", "</h2>"], "###": ["<h3>", "</h3>"], "####": ["<h4>", "</h4>"],
                "#####": ["<h5>", "</h5>"], "######": ["<h6>", "</h6>"], "+": ["<p>", "</p>"],
                "*": ["<code>", "</code>"]}


def get_mark_up(line):
    logger.debug("return: " + line.split(" ")[0])
    return line.split(" ")[0]


def trim_mark_up(line):
    return_string = ""
    for token in line.split(" ")[1:]:
        return_string += token + " "

    logger.debug("return: " + return_string.rstrip())
    return return_string.rstrip()


def line_has_markup(line):
    return get_mark_up(line) in allnote_html


def convert_to_html(allnote_tag, string):
    return_string = ""
    if allnote_tag in allnote_html:
        return_string = allnote_html[allnote_tag][0] + string + allnote_html[allnote_tag][1]

    logger.debug("return: " + return_string)
    return return_string


def process_input(input):
    output = ""
    tags = []
    text_elements = []
    for line in input:
        if line_has_markup(line):
            tags.append(get_mark_up(line))
            text_elements.append(trim_mark_up(line).rstrip())
        elif :
            text_elements[len(tags) - 1] += " " + line.rstrip()

    for tag, element in zip(tags, text_elements):
        output += convert_to_html(tag, element) + "\n"

    print(output)
    return output


def embed_in_html(input, title, stylesheet):
    html_begin = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n    <meta charset='UTF-8'>\n" \
                 "    <title>" + title + "</title>\n" \
                                         "    <link rel='stylesheet' href='" + stylesheet + "'>\n" \
                                                                                            "</head>\n<body>\n"
    html_end = "</body>\n</html>"

    return html_begin + input + html_end


def __main__():
    input_file = open("input.txt", "r")
    output_file = open("output.html", "w")
    output = process_input(input_file)
    output = embed_in_html(output, "example", "css/example.css")
    output_file.write(output)


__main__()


# Ich könnte auch wie in MD bereiche markieren statt ihn suchen zu lassen. ''' code '''
# Leere Zeilen sollen ignoriert werden
# Processing darf erst bei der letzten Zeile enden, momentan wird früher gestoppt
# Command-line tool draus machen
# New lines aus String entfernen! Vielleicht gibt es eine Python Anweisung dafür
# BEM einführen für besseres CSS
# Am Anfang des Dokuments Mit eigenem Tag Meta-Daten einbauen, zum Beispiel das zu verwendene Stylesheet.
# Ist kein Stylesheet gesetzt worden wird ein default-Stylesheet gewählt
# bei code darf kein whitespace verändert werden! Keine Einrückung oder newline
# erst mal ansehen wir <code> von html gerendert wird, vielleicht muss ich da kein <br> einfügen
# für newlines ohne Inhalt <br> einfügen
