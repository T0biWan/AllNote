# AllNote
As a student I take notes, a lot of notes!
I got tired of formating them over and over again in the same way.
At the same time I got to like Markdown and wanted to play a bit with it.

The result is this project where I made my own, super simple, mark up language and convert it into valid html.
Why not stay with Markdown? I wanted more freedom and the possibility to add new features as easy as possible.

Since the result is HTML my notes now get formatted by CSS and I only have to make the stylesheet ones.

## The Nameless Mark Up Language
So far these are the possible tags:
| AllNote-Tag | HTML_Tag |
|-------------|----------|
|      #      |   <h1>   |
|      ##     |   <h2>   |
|     ###     |   <h3>   |
|     ####    |   <h4>   |
|    #####    |   <h5>   |
|    ######   |   <h6>   |
|      +      |    <p>   |
|      *      |  <code>  |

## How to use AllNote
1. Take your notes with the given tags for example:
 # Heading
 ## Subheading
 + Some text
 Some more text
 Even more text

 ## Subheading
 + Some other text

 2. Convert your notes to HTML
 - Set the paths for in- and output
 - Give the HTML-Document an optional title and the path to your desired stylesheet
 ´´´ Python
 def __main__():
    input_file = open("input.txt", "r")
    output_file = open("output.html", "w")
    output = process_input(input_file)
    output = embed_in_html(output, "example", "css/example.css")
    output_file.write(output)
 ´´´
 - run the script