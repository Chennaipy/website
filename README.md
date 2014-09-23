# [Chennaipy](http://chennaipy.org/)

This is the repo for the Chennaipy, Chennai Python user group's
website [http://chennaipy.org](http://chennaipy.org).

## Find us

* [Meetup.com](http://www.meetup.com/chennaipy/)
* [Mailing list](https://mail.python.org/mailman/listinfo/chennaipy)

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
