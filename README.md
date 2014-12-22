# Chennaipy Website

[![Build Status](https://travis-ci.org/Chennaipy/website.svg?branch=master)](https://travis-ci.org/Chennaipy/website)

This is the repo for the Chennai Python User Group's website
[http://chennaipy.org](http://chennaipy.org). The site is built
using Pelican, a static site generator, powered by Python. The
site's theme is based on [Pure Pelican Theme](https://github.com/PurePelicanTheme/pure-single).

## Find us

* [Meetup.com](http://www.meetup.com/chennaipy/)
* [Mailing list](https://mail.python.org/mailman/listinfo/chennaipy)
* [Twitter](http://twitter.com/chennaipy)

## Setup

* Clone repo

        $ git clone git@github.com:<username>/<repo>.git        

* Set up a virtual env in that folder and activate it

        $ cd <repo>
        $ virtualenv env
        $ source env/bin/activate

* Install the requirements using `pip` from inside the virtual environment

        (env)$ pip install -r requirements.txt
        
* Start the server

        make devserver

## Contributing

See CONTRIBUTING.md
