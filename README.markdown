# LANDER :crescent_moon: :rocket:

***A small tool to compile static one-page pages from a template and some configuration files. :crescent_moon: :rocket:***

## About :books:

A while ago, I wanted to make a custom page-builder and I came up with this. This is a small tool to compile static one-page pages from a template and some configuration files.

## Download :inbox_tray:

Download this tool from [here]().

## Usage :hammer:

### Requirements

You need Python 3.x installed. That's it.

### Set it up

You need to create three parts.

- An HTML template.
- A configuration file.
- A content file.

An HTML template: In this file you would have a bunch of HTML code and some variables.
Variables would be of this form: `{{ variable }}`.

```text
<!DOCTYPE html>
<html>
 <head>
  <title>{{ title }}</title>
 </head>
 <body>
  <h1>{{ author }}</h1>
  <div class="content">
   {{ content }}
  </div>
  <div class="iter">
  </div>
 </body>
</html>
```

A configuration file: Here you set how each of the variables should be populated.
Example: `config.json`

```JSON
{
  "author":"Alexander Abraham",
  "title":"Sample page",
  "content":[
    "extern",
    "content.txt"
  ]
}
```

The first variable `author` is populated with `Alexander Abraham`.
The second variable `title` is populated with `Sample page`.
The third variable `content` is populated with the content from the content file `content.txt`.
This is signified by the `extern` keyword.

`content.txt` could look like this:

```text
Lorem ipsum sit dolor amet. Lorem ipsum sit dolor amet.
Lorem ipsum sit dolor amet. Lorem ipsum sit dolor amet.
Lorem ipsum sit dolor amet. Lorem ipsum sit dolor amet.
```

### Run it

- 1.) Download the tool.
- 2.) Open a command-line window in the same directory.
- 3.) Invoke the tool like this:

```bash
# Print out version information.
$ python3 lander.py --version
# Compile the HTML file with all variables filled in and print out the code that is generated.
$ python3 lander.py --config config.json --template template.html --verbose
# Compile the HTML file with all variables filled in.
$ python3 lander.py --config config.json --template template.html
# Compile the HTML file with all variables filled in with a custom file name.
$ python3 lander.py --config config.json --template template.html --output index.html
# Compile the HTML file with all variables filled in with a custom file name and print out the code that is generated.
$ python3 lander.py --config config.json --template template.html --output index.html --verbose
```

## Note :scroll:
