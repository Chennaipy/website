Title: February Meet Minutes
Date: 2016-04-18 00:00
Tags: Meeting Minutes
Summary: <img src="http://photos1.meetupstatic.com/photos/event/9/8/c/7/global_447399111.jpeg"/> <img src="http://photos1.meetupstatic.com/photos/event/9/9/0/2/global_447399170.jpeg"/> <img src="http://photos2.meetupstatic.com/photos/event/9/9/4/6/global_447399238.jpeg"> <img src="http://photos2.meetupstatic.com/photos/event/9/9/5/1/global_447399249.jpeg"/>

## Session 1: Extended Window Manager using xlib

Speaker: Rengaraj from Zilogic Systems

<a
href="http://photos2.meetupstatic.com/photos/event/9/8/c/7/highres_447399111.jpeg"><img
style="float:right; margin:0.5em" src="http://photos4.meetupstatic.com/photos/event/9/8/c/7/event_447399111.jpeg"></img></a>

Rengaraj started the session by giving overview of EWMH (Extended
Window Manager).  Explained about the architecture and sequence of
function flow to handle any window of an application. To facilitate
power of EWMH he put sample program using some of the EWMH APIs to
control windows that were open.

Followed by Rengaraj session on EWMH audience discussed usage of it in
real time. One of them used it at client place to avoid system in
single screen for a longer duration. He used EWMH to switch to various
screen in random manner.

## Session 2: Analysis of Algorithm

Speaker: Ashok

<a
href="http://photos4.meetupstatic.com/photos/event/9/9/0/2/highres_447399170.jpeg"><img
style="float:right; margin:0.5em"
src="http://photos4.meetupstatic.com/photos/event/9/9/0/2/event_447399170.jpeg"></img></a>

Ashok started his note with need for analysis for algorithm and
various parameters like time, space complexities to be considered in
analysis of algorithm. Sequence of his session segment was on theory
followed by practical working of theory and at the end with evaluation
of result.  Explain various algorithm complexity measuring concepts
like Big O, Small O, Theta, Big Omega, Small Omega. Their usefulness,
application need were explained in detail. It was widely accepted that

  1. Big O and Small O were used in measuring worst case scenarios

  2. Big and Small Omega were used in measuring best case scenarios
    
Fibonacci series was taken as an example program to evaluate
algorithm. Two implementations were taken for evaluation Iterative and
Recursive were taken as example to evaluate.  Program was return in
python while execution it was observed that iterative method was
linearly complex where as recursive was exponentially complex. In a
larger set, Recursive took twice the time of iterative method.

## Session 3: Experimental Mathematics with Python and Sage

Speaker: Professor Amritanshu Prasad

<a
href="http://photos1.meetupstatic.com/photos/event/9/9/4/6/highres_447399238.jpeg"><img
style="float:right; margin:0.5em"
src="http://photos1.meetupstatic.com/photos/event/9/9/4/6/event_447399238.jpeg"></img></a>

Professor Amritanshu started the session with full of
enthusiasm. Being an academician in math, his session was focused on
how sage library simplified some of the complex computation were made
easy. He used problem of identifying number of odd numbers in a
binomial coefficient. The sequence of numbers followed a
pattern. Professor explained the pattern formation using pascal's
triangle. Relation of reoccurrences in pascal's triangle were
explained well.

Integer partition was analyzed number of ways an integer can be split
for e.g., 5 can be split by as shown below

                      5 = 5
                        = 4 + 1
                        = 3 + 2
                        = 3 + 1 + 1
                        = 2 + 2 + 1
                        = 2 + 1 + 1 + 1
                        = 1 + 1 + 1 + 1 + 1

Occurrences of odd numbers were taken for analysis and its been
observed that occurrences appeared in pattern Power of 2.

End of it we observed how sage library was used in computing
mathematical problems with ease. Material can be downloaded from the
link
[http://www.imsc.res.in/~amri/experimental_math.pdf](http://www.imsc.res.in/~amri/experimental_math.pdf)

## Session 4: Need for Object oriented programing

Speaker: Vijay Kumar

<a
href="http://photos1.meetupstatic.com/photos/event/9/9/5/1/highres_447399249.jpeg"><img
style="float:right; margin:0.5em"
src="http://photos1.meetupstatic.com/photos/event/9/9/5/1/event_447399249.jpeg"></img></a>

Vijay took an example of implementing circular buffer to explain the
need for Object orientation programing.

First he implemented one circular buffer using simple function.
Second a need for 2nd buffer came to existence. This was solved using
dictionary in python.  Third though usage of dictionary solved the
reuse to an extent. Readability, maintenance and extendibility were
observed tough to take care. This brought usage of classes to
implement circular buffer. As an extension of class implementation
constructor / initialization of objects were detailed using `__init__`
function. Followed by it implicit presence of object instance were
shown using self inside class functions.

Code to vijay session can be found in
[https://github.com/zilogic-systems/workshop-sessions/tree/master/python-oop](https://github.com/zilogic-systems/workshop-sessions/tree/master/python-oop)

## Lightning talk

  1. Porting of SQL to no SQL DBs using mongo DB was explained by
     one of the audience

  2. http://www.unnati.xyz and datascience workshop scheduled in
     Bangalore was explained by Shreyas.

## Credits

Thanks to [Babu](http://www.meetup.com/Chennaipy/members/177868122/)
for the beautiful photos. And thanks to
[Sampath](http://www.meetup.com/Chennaipy/members/188158663/) for the
meeting minutes.