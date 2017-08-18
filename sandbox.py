import logging
import sys

# create and configure logger
LOG_FORMAT = '%(levelname)s:%(funcName)s:%(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, filemode='w', format=LOG_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

allnote_html = {"#": ["<h1>", "</h1>"], "##": ["<h2>", "</h2>"], "###": ["<h3>", "</h3>"], "####": ["<h4>", "</h4>"],
                "#####": ["<h5>", "</h5>"], "######": ["<h6>", "</h6>"], "+": ["<p>", "</p>"],
                "*": ["<code>", "</code>"]}


def get_mark_up(string):
    logger.debug("return: " + string.split(" ")[0])
    return string.split(" ")[0]


def trim_mark_up(string):
    return_string = ""
    for token in string.split(" ")[1:]:
        return_string += token + " "

    logger.debug("return: " + return_string.rstrip())
    return return_string.rstrip()


def line_has_markup(line):
    return get_mark_up(line) in allnote_html


def convert_to_html(string, allnote_tag):
    return_string = ""
    if allnote_tag in allnote_html:
        return_string = allnote_html[allnote_tag][0] + string + allnote_html[allnote_tag][1]

    logger.debug("return: " + return_string)
    return return_string


def process_input(input):
    output = ""
    current_string = ""
    allnote_tag = ""

    for line in input:
        if line_has_markup(line):
            if current_string != "":
                output += convert_to_html(current_string, allnote_tag) + "\n"
            allnote_tag = get_mark_up(line)
            current_string = trim_mark_up(line)
        else:
            current_string += " " + line
    if current_string != "":
        output += convert_to_html(current_string, allnote_tag)

    return output


def __main__():
    output_file = open("output.txt", "w")
    input_file = open("input.txt", "r")
    output = process_input(input_file)
    output_file.write(output)


__main__()


# Ich könnte auch wie in MD bereiche markieren statt ihn suchen zu lassen. ''' code '''
# Leere Zeilen sollen aber ignoriert werden
# Command-line tool draus machen
# New lines aus String entfernen! Vielleicht gibt es eine Python Anweisung dafür
# BEM einführen für besseres CSS
