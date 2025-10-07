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

## Setup for local development

### Prerequisites

Python 3.8+

### Using UV (Recommended)

UV is a fast Python package installer and resolver.

#### Install UV (if you haven't already)

* For macOS and Linux

        $ curl -LsSf https://astral.sh/uv/install.sh | sh

* For windows

        $ powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

#### Fork repo

  [Fork](https://github.com/Chennaipy/website/fork) the repository to your account
so that you have your copy of the website.

#### Clone repo

        $ git clone --recursive git@github.com:<your-username>/website.git chennaipy-website
<br>

        $ git submodule update --init --recursive
  
  This will clone the repository on to your system and clone the submodules inside
it as well recursively. Additionally, the folder to which it will be cloned to
is called `chennaipy-website`.

#### Set up the project with UV

        $ cd chennaipy-website
        $ uv venv
        $ source .venv/bin/activate  # On Windows: .venv\Scripts\activate

#### Install the project with UV (this will install dependencies and set up the web command)

        $ uv sync

#### Start the server

        $ uv run dev

  Or specify a custom port:

        $ uv run dev -p 3000

#### Visit local site

  Open up your web browser and point it to [http://localhost:8000](http://localhost:8000) to see the site
running locally. Yay!

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)
