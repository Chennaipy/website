Title: Feb 2017 Meetup Minutes
Date: 2017-02-25 15:00
Tags: Meeting Minutes
Summary: <img src="https://a248.e.akamai.net/secure.meetupstatic.com/photos/event/c/4/a/global_458703146.jpeg" alt=""/> <img src="https://a248.e.akamai.net/secure.meetupstatic.com/photos/event/c/6/8/global_458703176.jpeg" alt=""/> <img src="https://a248.e.akamai.net/secure.meetupstatic.com/photos/event/c/3/a/global_458703130.jpeg" alt=""/>

### A Gentle Intro to Types by Shrayas Rajagopal

<a
href="https://a248.e.akamai.net/secure.meetupstatic.com/photos/event/c/4/a/600_458703146.jpeg">
<img
src="https://a248.e.akamai.net/secure.meetupstatic.com/photos/event/c/4/a/event_458703146.jpeg"
alt="Shrayas Presenting his Talk"/> </a>

Shrayas started by building on the basics to introduce more advanced concepts later on.
- What are types?
    - Class of value
    - Set of operations

- Why Types?
    - Humans make a lot of errors
    - Computers are very good at repeating things
    - Types help them to bring it together. Helps reduce the number of mistakes

- Type Systems
    - Think of them like magic boxes
    - They run through the source code
    - Check if the program makes sense given the set of operations (rules)

- Dynamic Typing vs Static Typing
    - General myth that static has types and dynamic means no types
    - He explained that both actually have types.
    - Static languages get to know about the type at compile time
    - Dynamic languages get to know about the type at runtime
    - He then showed examples where errors where caught during compile time in C# but went undetected until runtime in Python

- Advantages and Disadvantages of both based on the following criteria
    - Hackable or not (easy to get started and build things)
    - Readability
    - Iteration speed 
    - Enforces tests or not
    - Size of code base

- Gradual Typing
    - Advantages of both
    - Runtime fluidity marries compile time rigidity
    - Some languages / frameworks with gradual typing
        - Hack
        - Typescript
        - mypy

- Why Gradual Typing?
    - Rigidity
    - Better dev tools
    - Readability
    - Conscise code base
    - It is possible to migrate your codebase to gradual typing in part


### GUI Using Python by Gaurav Sehrawat
Gaurav went over the following:-

- Basic Info
    - tkinter is a Python interface to Tcl/Tk
    - Tcl/Tk is cross platform
    - Tcl is a dynamic language. Tk is an extension provided for development of GUIs
    - Uses native system APIs
    - Each GUI is basically a collection of frames. Each frame has a layout manager
    - The IDLE editor is built using Tkinter

- Python 2 vs Python 3
    - Very easy to port Tkinter code. It's very similar across both 2 & 3
    - Letter casing is different or it is has a prefix

- Geometry Manager or Layout Manager
    - Specify relations with respect to other elements
    - Pack (simple layout manager)
    - Grid (table like)

- When to Use Pack
    - Simple geometry like up, down etc
    - Side by Side
    - Element go on top of each other

- If you need something more complex and specific it's always better to go with grid.

- Widget List
    - Labels
    - Buttons
    - Dialog Boxes etc

- He showed the following examples
    - Hello, World
    - Pack 
    - Grid
    - Events and bindings
    - Dialog Boxes
    - Matplot lib 
    - Matplot lib dynamic plots using changes in real time data
    - opencv

### Networking Tea Break sponsored by [InkMonk](http://inkmonk.com/)

<a
href="https://a248.e.akamai.net/secure.meetupstatic.com/photos/event/c/6/8/600_458703176.jpeg">
<img
src="https://a248.e.akamai.net/secure.meetupstatic.com/photos/event/c/6/8/event_458703176.jpeg"
alt="Section of members gathered"/> </a>

### YAML Validation in Python by Vijay Kumar

- He quicly went over the basics
    - Different methods of representing data
    - Impacts of representation

- Benefits of text representation
    - Easy to create
    - Easy to use Version Control Systems
    - Easy to review

- Explained about Asciidoc. Humans can enter text. It then converts it to other formats using toolchains

- Types of Data
    - Structured Data
        - Structures that are easy for computers to understand but difficult for humans
        - They can be manipulated by the computer easily
        - Example arrays, Databases
    - Unstructured Data
        - Human oriented
        - Harder for machines to work with such data
        - Eg Word Documents
    - Semi Structured Data
        - Easy for both computers and humans
        - Eg:- XML, JSON, YAML 
        - It undergoes an additional step like parsing
- YAML
    - Superset of JSON
    - Syntax and things possible
    - Examples of YAML that helps him organise ChennaiPy

- Roadblocks to using YAML
    - Human input prone to errors
    - Proper validation is key

- Difficulties in validation YAML
    - Writing code that handles verification is hard
    - No schema available for YAML
    - Examples of nasty error messages thrown when validation fails

- Using jsonschema to validate YAML thus giving better error checking and friendlier prompts

### Lightning Talk by Ashok Govindarajan
He spoke about his broad top level views on Machine Learning.  

- Born out of pattern recognition
- Mostly comprises of curve fitting, adapt, predict and recommend
- Why the sudden rise in Machine Learning?
    - There from quite a long time
    - Sudden rise due to faster hardware, more storage and lots of good sources of data
- Role of low cost sensors
- Machine learning preceeds / enables decision making
- Helps in intuition to data driven decisions

### Credits

Vijay thanked Inkmonk for sponsoring the venue and Zilogic Systems for sponsoring the projector.

### Group Photo

<a
href="https://a248.e.akamai.net/secure.meetupstatic.com/photos/event/c/3/a/600_458703130.jpeg">
<img
src="https://a248.e.akamai.net/secure.meetupstatic.com/photos/event/c/3/a/event_458703130.jpeg"
alt="Group Photo"/> </a>


