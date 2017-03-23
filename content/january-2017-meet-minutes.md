Title: January 2017 Meetup Minutes
Date: 2017-01-28 15:00
Tags: Meeting Minutes
Summary: <img src="https://a248.e.akamai.net/secure.meetupstatic.com/photos/event/1/f/c/1/event_459368129.jpeg" alt=""/>

### PyShark in Network Packet Analysis by Rengaraj
Rengaraj's talk covered a way to analyse network requests in Python. He also explained about tools that PyShark is built on.

- Wireshark -> GUI tool for network analysis.
- TShark -> A command line tool for network analysis. It uses dumpcap to analyse TCP dump. It is used for:-
    - Layer by layer scrutiny.
    - Integration testing.
- PyShark is a wrapper around TShark.
- Explained the ping protocol in depth so that the audience could understand the example he would present later.
- PyShark example
    - He bought an example file from a ping request he had made at home.
    - Analysed it using PyShark.
    - Showed a few examples like display-filters etc


### Web Testing Framework in Python by Abhirath Mahipal
Abhirath went over the following:-

- Explained the need of a testing framework that uses Lisp to write test cases when he interned at LogicSoft.
- A small demo of the application -> The frontend GUI and report generation.
- JSON vs YAML vs Lisp to write test cases. Advantages and disadvantages of each.
- Lists vs Dictionaires and their implications on writing test cases.
- Using hylang to write Lisp that is understood by the Python interpreter.
- Some links that he shared.
    - [Peter Norvig's Lisp Parser in Python](http://norvig.com/lispy.html)
    - [Learn Lisp by building small applications. Free ebook](http://www.gigamonkeys.com/book/)

### Networking Tea Break

### Write Better Code by Anna Philips
Anna's talk covered topics like PEP8, PEP20 and PEP257 that stress on writing more Pythonic code. She also compared Pythonic solutions to other languages like C++ and Java. It covered examples and explanations for the following:-

- Key takeaways
    - PEP8 compliant code. It has a few rules to follow.
    - PEP20. Also called Zen of Python. Properties of code. Subjective and no definite steps.
    - PEP257. Docstring conventions.
- Idiamatic Python is normally faster
- in and not in operators
- unpacking sequences, swapping variables
- Some functions and constructs to create elegant looping constructs
    - enumerate (iterate easily with index and value)
    - reverse
    - sorted
    - looping over keys and values using dict.item
- Better ways to get and set values in a dictionary
    - dict.get()
    - dict.setdefault()
- List comprehensions
- "".join vs string concatenation
- Some constructs and data structures for efficiency
    - Lazy loading with generators
    - deques and pop vs list and deletes

### Lightning Talk by Gaurav Sehrawat
Gaurav mentioned a few resources to stay updated and find Python libraries in the domain you are working on. He also mentioned a few podcasts that are worth listening to. Some links that he shared:-
- awesome-python.com
- talkpython.fm
- changelog.com

### Lightning Talk by Vijay Kumar and Shrayas Rajagopal
Vijay went over problems that newbies might have while representing stuff in Python.

For example a student can be represented by a list, a dict and also as an object. He mentioned that thinking in terms of another language (like Java but not limited to Java) might help solve the issue. Also pointed out that if they need to have methods for that particular data it's better to use a class.

Shrayas gave insights that might help a programmer while choosing between a function and class to solve a problem.

- Gave a small example of a counter. Since the counter has a state it is better to use a class and encapsulate the count variable within the class rather than creating a function and using a global variable to maintain the count. Also there exists a possibility of more than one counters and hence global variables might prove to be a bad decision.
- It is better to use functions when output will remain the same for a given input. He quoted the example of the square function. No matter when you supply the input, the output will remain the same regardless.

Vijay and Shrayas also stressed on the fact that functions and classes are better than global variables.

### Group Photo

<img src="https://a248.e.akamai.net/secure.meetupstatic.com/photos/event/1/f/c/1/600_459368129.jpeg" alt="Group Photo"/></img>