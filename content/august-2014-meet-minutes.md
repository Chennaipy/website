Title: August Meet Minutes
Date: 2014-08-27 02:05
Tags: Meeting Minutes

This time around we had about 14 members attending the meet. The meet
started with the first talk -- "Unit Tests with Nose".

## Unit Tests with Nose

Vengatesh presented the various features of nose framework, comparing
them with the 'unittest' module present in the standard library. He
showed how the nose framework did not require us to create a separate
class for writing simple test functions, but still allowed for
providing test fixtures through decorators. He also should how more
complex test cases can be defined through test classes and test
packages. He then listed the plugins available with the nose
framework, and demonstrated the usage of the coverage plugin.

That brought us almost to the end of the talk, the next talk was "API
Documentation with Sphinx and Napoleon".

## API Documentation with Sphinx and Napoleon

Aadhithyan explained the usage of Sphinx and Napoleon. He showed:

  1. How Sphinx can be invoked using the 'sphinx-quickstart' command.
  2. The purpose of various files and folders created by the command.
  3. How the Napoleon plugin can be enabled, in the 'config.py' file.
  4. How the 'sphinx-apidoc' is to be invoked to create the
     reStructuredText files from the python modules.
  5. How the 'make' is to be invoked to create the html files from the
     reStructuredText

He demonstrated the above instructions with a simple Python module,
and more complex example, exercising all the features of the Google
docstring convention.

The discussion then moved on to, how the Google docstring convention
was better than the default one in Sphinx. With the Google docstring
convention, the docstring was both human readable and machine
readable.

That brought us to the end of the talk. The next talk was on "Brython".

## Brython

Vijay started off by explaining that Brython was a Python to Javascript
compiler written in Javascript. This allowed Python programs to be
executed within a browser. He then demonstrated an example Hello
World program shown below. When the HTML file was opened in a browser,
the "Hello World" message appeared in the Javascript console.

    <html>
      <head>
        <title>Brython Example</title>
        <script src="brython/brython.js"></script>
      </head>
      <body onload="brython()">
        <script type="text/python">
        print("Hello World")
        </script>
        <h1>Brython Example</h1>
      </body>
    </html>

He then modified the program step by step adding more and more
features, till it became an arithmetic quiz.

  Step 1. Display the "Hello World" message within the HTML page,
  instead of the Javascript console.

  Step 2. Use a separate file for the Python script, using 'src'
  attribute of the 'script' tag.

  Step 3. Display an arithmetic quiz question, with an input box.

  Step 4. Verify the answer entered, and display the next question.

  Step 5. Cleanup previous questions, before displaying the next
  question.

He then showed an example of paddle ball game, again building it step
by step from scratch. This time he used the canvas HTML element, to do
the graphics.

He concluded his talk with some real world use-cases for Brython. One
of the use-cases he showed was the Reeborg's World
http://reeborg.ca/index_en.html

## Asciinema

Rengaraj did a quick lightning talk on Asciinema, an open source
solution for recording terminal sessions. Rengaraj recorded a terminal
session uploaded it to Asciinema, played it back on Asciinema's
website. The recording, it seems, captures the VT100 escape sequences
instead of the on-screen pixels, which is what a conventional screen
capture program does. The advantage:

  1. Uploads are terribly fast.
  2. Download and playback is fast.
  3. No blurring in the playback.

## Merger with Pych

Vijay then provided an update on the merger with Pych. It seems that
Pych, was conceived to develop open source software using Python. And
Sam from Pych believes that their goals are much different from a
Python User Group, and it would be better for them to be a separate
entity.

But, since Pych is also organizing monthly meets, Vijay suggested that
we go with bi-monthly meets to avoid duplicating efforts. And the
members gathered agreed that this should be OK. He also suggested that
we spend the spare time that we get out of reducing the meetings, be
used to develop content for workshops and to organize workshops.

A few other suggestions that members came up with, were to create
meetup.com group for Chennaipy. Vijay agreed that, a meetup group
would be useful, and said he will be creating one for Chennaipy
shortly.
