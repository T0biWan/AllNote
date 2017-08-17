import logging
import sys

# create and configure logger
LOG_FORMAT = '%(levelname)s:%(funcName)s:%(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, filemode='w', format=LOG_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

allnote_html = {"#": ["<h1>", "</h1>"], "##": ["<h2>", "</h2>"], "###": ["<h3>", "</h3>"], "####": ["<h4>", "</h4>"],
                "#####": ["<h5>", "</h5>"], "######": ["<h6>", "</h6>"], "+": ["<p>", "</p>"], "*": ["<code>", "</code>"]}



def get_mark_up(string):
    logger.debug("return: "+string.split(" ")[0])
    return string.split(" ")[0]


def trim_mark_up(string):
    return_string = ""
    for token in string.split(" ")[1:]:
        return_string += token + " "

    logger.debug("return: "+return_string.rstrip())
    return return_string.rstrip()


def convert_to_html(string, allnote_tag):
    return_string = allnote_html[allnote_tag][0] + string + allnote_html[allnote_tag][1]
    logger.debug("return: " + return_string)
    return return_string


def process_input(string):
    mark_up = get_mark_up(string)
    string = trim_mark_up(string)
    return convert_to_html(string, mark_up)


def __main__():
    output_file = open("output.txt", "w")
    input_file = open("input.txt", "r")
    for line in input_file:
        output_file.write(process_input(line)+"\n")


__main__()

# Er soll immer bis zum nächsten allnote-tag suchen
# Leere Zeilen sollen aber ignoriert werden
# Command-line tool draus machen
