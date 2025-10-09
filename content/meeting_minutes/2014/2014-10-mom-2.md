Title: October Meet Minutes
Date: 2014-10-27 10:45
Tags: Meeting Minutes
Summary: <img alt="" src="http://photos2.meetupstatic.com/photos/event/4/b/5/d/global_432439293.jpeg"/> <img src="http://photos2.meetupstatic.com/photos/event/4/c/3/8/global_432439512.jpeg" alt=""/> <img src="http://photos2.meetupstatic.com/photos/event/5/3/8/9/global_432441385.jpeg" alt=""/>

## Python Test Automation

<a
href="http://photos2.meetupstatic.com/photos/event/4/b/5/d/highres_432439293.jpeg"><img
src="http://photos2.meetupstatic.com/photos/event/4/b/5/d/event_432439293.jpeg"
alt="Krishnan Explaining" style="float: right"></img></a>

The first talk of the evening was given by Krishnan in Python Test
Automation. He explained how Python could be used for all types of
testing - web testing, GUI testing, functional testing, unit testing,
embedded testing etc. He explained how Python was a good choice for
test automation, because it allowed you to use the same language for
all the different types of testing, in contrast to specific automation
test software, each specialised in one type of testing, and each
requiring a different tool language to be learnt.

He then went on to list useful python modules for testing, some of which are 

  * `shutil` - for copying files quickly
  * `subprocess` - for running another process from your program, and
    monitoring its status, getting and using its output
  * `pexpect` - for interacting with console applications
  * `logging` - for logging, but where u can specify different levels of
    errors, like debug, error, warning and critical
  * `unittest` - for writing unit tests 
  * `regex` - 
  * `pep8` and `pylint` - for checking if your source code confirms to
    python coding standards
  * `traceback` and `pdb` - standard python debugging libraries to step
    through your code.
  * `pywinauto` - for automating windows tasks, including installations!

Two other interesting things mentioned were image based automation and
the difference between unittests and integration tests.
 
In image based automation you automate windows tasks like clicking a
shortcut, emptying the recycle bin by getting the object you want to
automate by searching for it through its image, rather than through
the windows API or some other dictionary/list.

Unit tests are where you check each and every part of the code
separately for its functionality, error conditions etc. Integration
testing is where you check one module of the code for its ability to
work properly with other outside objects. Each module then acts like a
black box, and you are more concerned about its working with other
modules rather than how the module itself works ie: whats inside the
black box

## Docopt

<a
href="http://photos2.meetupstatic.com/photos/event/4/c/3/8/highres_432439512.jpeg"><img
src="http://photos2.meetupstatic.com/photos/event/4/c/3/8/event_432439512.jpeg"
alt="Rengaraj Explaining" style="float: right"></img></a>

The second talk was given by Rengaraj on Docopt. Docopt is a python
module used to generate an interface for your command line
application. it also automatically generates a parser for it. I had
some confusion on where this module could be used, so I went back home
and checked it out. Basically, you can use it to easily create a
command line program where you can give options like -v, -x -u and -uv
following your command. The great thing about Docopt is that it will
then create a dictionary with your options as keys and the options the
user put as values to those keys, so that you can easily find out the
user input commands were. Its much much easier than other similar
functional modules like optparse. The only thing to remember with
Docopt is that the usage format has to be in the POSIX format for it
to work

## Building Embedded Systems with Twisted

<a
href="http://photos2.meetupstatic.com/photos/event/5/3/8/9/highres_432441385.jpeg"><img
src="http://photos2.meetupstatic.com/photos/event/5/3/8/9/event_432441385.jpeg"
alt="Vijay Explaining" style="float: right"></img></a>

The last talk was given by Vijay Kumar on a problem he solved at his
company using Python and some embedded hardware. He explained how at
his company they were faced with the problem of keeping track of who
had borrowed common resources and of getting the person who had
borrowed it to return the resource after he/she had used it. After
trying simple solutions like keeping a notebook, reminding people, and
finding that they did not work, they finally decided to use a tech
solution. They used an RFID reader and put an RFID tag on each
resource and linked it to a server so that they would know who had
borrowed which resource. Python was used to interface and talk to the
hardware, which included a reed switch, RFID reader, and the
server. The Python framework used was Twisted, and one interesting
thing was the idea of an event driven framework, instead of a blocking
read/write framework. It was nice to see the actual hardware, software
and also a video of the system in action! Vijay also showed us the
state machine of the system which showed the various states of the
system and how it changed depending on the users actions.

## Credits

  * Venue Coordinator: Shrinivasan 
  * Networking over Tea, Sponsor: Clay Labs 
  * Marketing: Krishnan Shankar, Prasanna Venkadesh, Chintu Philips, Shrinivasan 
  * Photographs: Krishnan Shankar, Kenash Kanagaraj 
  * Minutes: Harsha