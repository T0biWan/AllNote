# AllNote
As a student I take notes, a lot of them!
I got tired of formatting them over and over again to make them more appealing for a re-read.
At the same time I got to like Markdown and wanted to play a bit with it.

The result is this project where I made my own, super simple, mark up language and convert it, with Python,
into valid html.
Yyu will notice that I oriented and borrowed from Markdown since it is so simple and clever made
Why not stay with Markdown? I wanted more freedom and the possibility to add new features as easy as possible.

Since the result is HTML my notes now get formatted by CSS and I only have to make the stylesheet ones.
If I don't like anymore it, I can just change the CSS or use different stylesheets for different topics.

## The Nameless Mark Up Language
So far these are the possible tags:
- AllNote-Tag - HTML-Tag
- \#      - \<h1>
- \##     - \<h2>
- \###    - \<h3>
- \####   - \<h4>
- \#####  - \<h5>
- \###### - \<h6>
- \+      - \<p>
- \*      - \<code>
- \++text++ - \<br>

## How to use AllNote
1. Take your notes with the given tags for example:
```
# Heading
## Subheading
+ Some text
Some more text
Even more text

## Subheading
+ Some other text
```

2. Convert your notes to HTML
- Set the paths for in- and output
- Give the HTML-Document an optional title and the path to your desired stylesheet
 ```python
 def __main__():
    input_file = open("input.txt", "r")
    output_file = open("output.html", "w")
    output = process_input(input_file)
    output = embed_in_html(output, "example", "css/example.css")
    output_file.write(output)
 ```
- run the script
- Get yourself some HTML
```html
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>example</title>
    <link rel='stylesheet' href='css/example.css'>
</head>
<body>
<h1>Heading</h1>
<h2>Subheading</h2>
<p>Some Text</p>
<h2>Subheading</h2>
<p>Some more Text</p>
<code>Code 0 Code 1 Code 2 </code>
<p>Text0 Text1 Text2 Text3  Text4 Text5</p>
</body>
</html>
```