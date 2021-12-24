# LANDER :crescent_moon: :rocket:

***A small tool to compile static one-page pages from a template and some configuration files. :crescent_moon: :rocket:***

![GitHub CI](https://github.com/iamtheblackunicorn/Lander/actions/workflows/python.yaml/badge.svg)

## About :books:

A while ago, I wanted to make a custom page-builder and I came up with this. This is a small tool to compile static one-page pages from a template and some configuration files.

## Project page :rocket:

Lander's project page can be found [here](https://blckunicorn.art/Lander).

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

```HTML
<!DOCTYPE html>
<!--
Lander by Alexander Abraham.
Licensed under the MIT license.
Project link:
https://github.com/iamtheblackunicorn/Lander
-->
<html>
 <head>
  <link rel="apple-touch-icon" sizes="57x57" href="https://blckunicorn.art/assets/favicon/apple-icon-57x57.png">
  <link rel="apple-touch-icon" sizes="60x60" href="https://blckunicorn.art/assets/favicon/apple-icon-60x60.png">
  <link rel="apple-touch-icon" sizes="72x72" href="https://blckunicorn.art/assets/favicon/apple-icon-72x72.png">
  <link rel="apple-touch-icon" sizes="76x76" href="https://blckunicorn.art/assets/favicon/apple-icon-76x76.png">
  <link rel="apple-touch-icon" sizes="114x114" href="https://blckunicorn.art/assets/favicon/apple-icon-114x114.png">
  <link rel="apple-touch-icon" sizes="120x120" href="https://blckunicorn.art/assets/favicon/apple-icon-120x120.png">
  <link rel="apple-touch-icon" sizes="144x144" href="https://blckunicorn.art/assets/favicon/ms-icon-144x144.png">
  <link rel="apple-touch-icon" sizes="152x152" href="https://blckunicorn.art/assets/favicon/apple-icon-152x152.png">
  <link rel="apple-touch-icon" sizes="180x180" href="https://blckunicorn.art/assets/favicon/apple-icon-180x180.png">
  <link rel="icon" type="image/png" sizes="192x192"  href="https://blckunicorn.art/assets/favicon/android-icon-192x192.png">
  <link rel="icon" type="image/png" sizes="32x32" href="https://blckunicorn.art/assets/favicon/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="96x96" href="https://blckunicorn.art/assets/favicon/favicon-96x96.png">
  <link rel="icon" type="image/png" sizes="16x16" href="https://blckunicorn.art/assets/favicon/favicon-16x16.png">
  <link rel="manifest" href="https://blckunicorn.art/assets/favicon/manifest.json">
  <meta name="msapplication-TileImage" content="/assets/favicon/ms-icon-144x144.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Lander for Python, a small tool to compile static one-page pages from a template and some configuration files."/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pushster&display=swap" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="https://blckunicorn.art/assets/stylesheets/lander.css"/>
  <title>{{ title }}</title>
 </head>
 <body>
  <h1>{{ author }}</h1>
  <div class="content">
   <p>
   {{ content }}
  </p>
  <p>
   Source: {{ project_link }}
  </p>
  </div>
 </body>
</html>
```

A configuration file: Here you set how each of the variables should be populated.
Example: `config.json`

```JSON
{
  "author":"Lander",
  "title":"Lander",
  "content":[
    "extern",
    "example/content.txt"
  ],
  "project_link":"https://github.com/iamtheblackunicorn/Lander"
}
```

The first variable `author` is populated with `Alexander Abraham`.
The second variable `title` is populated with `Sample page`.
The third variable `content` is populated with the content from the content file `content.txt`.
This is signified by the `extern` keyword.

`content.txt` could look like this:

```text
Welcome to Lander v.1.0! A small static-site generator written in Python 3.
Use the link below to find out more about Lander. All instructions and guidelines
are in the project's "README".
```

### Run it

- 1.) Download the tool.
- 2.) Open a command-line window in the same directory.
- 3.) Invoke the tool like this:

```bash
# Print out version information.
$ python3 lander.py --version
# Initialize a new project in a directory called "example".
# This will create files as in the example above in "example".
# Customize the files to your liking. :)
$ python3 lander.py --init example
# Compile the HTML file with all variables filled in and print out the code that is generated.
$ python3 lander.py --config config.json --template template.html --verbose
# Compile the HTML file with all variables filled in.
$ python3 lander.py --config config.json --template template.html
```

If you run any of the last two commands in a command-line window, you will see a little file called `index.html` in a directory called `build`.

## Note :scroll:

- *Lander :crescent_moon: :rocket:* by Alexander Abraham :black_heart: a.k.a. *"The Black Unicorn" :unicorn:*
- Licensed under the MIT license.
