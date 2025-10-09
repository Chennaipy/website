Title: October Meet Minutes
Date: 2015-11-19 00:00
Tags: Meeting Minutes
Summary: <img src="http://photos2.meetupstatic.com/photos/event/c/9/5/3/global_443691539.jpeg"/> <img src="http://photos1.meetupstatic.com/photos/event/c/8/c/6/global_443691398.jpeg"/> <img src="http://photos3.meetupstatic.com/photos/event/c/9/1/c/global_443691484.jpeg"/>

Meet-up held on sunny pleasant day, with auditorium filled with
audience ready for talks as Vijay Kumar outlined the purpose of
meet-up and agenda.

## Postgres Explain

<a
href="http://photos2.meetupstatic.com/photos/event/c/9/5/3/highres_443691539.jpeg"><img
src="http://photos2.meetupstatic.com/photos/event/c/9/5/3/event_443691539.jpeg"/></a>

First talk was given by Abishek Postgresql "EXPLAIN". He started with
general audience poll on query optimization and query performance. He
then explain the usage of "EXPLAIN" which verify our speculation and
gives us cost of query while "EXPLAIN ANALYSE" actually runs the query
and gives cost of query. He explained the anatomy of "EXPLAIN" output
and described startup cost and end cost, where end cost is what we
generally take into consideration.

His talks consisted riddles in form of audience polls. One riddle was
with filters whether "WHERE" would result in low cost or not. Infact
"WHERE" clause increases the cost. Another riddle followed, whether
creating "INDEX" on query would optimize the query or not. Result was
surprising since "INDEX" didn't reduce the cost, it's because low
cardinality indexes are ignored. Next quiz was on "JOIN", adding
"INDEX" on "JOIN" clause also doesn't improve the cost. In fact "JOIN"
doesn't use index in any step, to improve efficiency for "JOIN" better
idea would be to use filter clause on one of the table.  The last quiz
included "ORDER BY", adding "INDEX" while using "ORDER BY" clause
really improves the cost, which was the key take away from the talk.

## Introduction to pgcli and mycli

Next talk by amjith(@amjithr) complemented the previous one in huge
way by adding CLI tool for postgresql queries. He is the author of
pgcli(pgcli.com) and mycli(mycli.net). He right away got into demo of
pgcli. He demoed auto completion feature with fuzzylogic
completion. Syntax highlight and meta commands completion were also
incentives of pgcli. PGCLI don't need semicolons for one line commands
while multiline mode needs them.  Talk was purpose wasn't to introduce
to his tools, he wanted to dissipate knowledge on building tools for
modern CLI. He introduced tools which would help in building on CLI
tools including PTPYTHON which is awesome python repl, WHARFEE which
is docker shell interface, SAWS which is wonderful for AWS shell
interface and PYVIM which is Vim clone in Python. He further
introduced PROMPT TOOLKIT which is helpful in auto-completion and
PYGMENTS which is helps in syntax highlighting. He also introduces
fuzzy-finder algorithm built by him and a blog post regarding the
same. CLICK is also nice tool for CLI helper methods. He concluded the
talk with question from audience and his contact details.

## Networking Tea Break

<a
href="http://photos1.meetupstatic.com/photos/event/c/8/c/6/highres_443691398.jpeg"><img
src="http://photos1.meetupstatic.com/photos/event/c/8/c/6/event_443691398.jpeg"/></a>

## Image Processing using OpenCV

Next talk was by HariPriya Bhaskar on OpenCV. She started her talk
with an inspiring self-driving car video which has application of
OpenCV. She then headed over to short demo of object tracking using
HSV value parameter. She then explained the corresponding code used in
the demo of object tracking. She ended her talk with another video on
future concept of applications of OpenCV in augmented reality
domain. On taking questions from audience she in-depth explained the
"GAIT" analysis in her project, in her clinical project she used
handy-cam and OpenCV for tracking movement of patient to give them
feedback. Shrayas further added to info about "GAIT" analysis used by
professional athletes.

## Pretty Printing in Python

<a
href="http://photos3.meetupstatic.com/photos/event/c/9/1/c/highres_443691484.jpeg"><img
src="http://photos3.meetupstatic.com/photos/event/c/9/1/c/event_443691484.jpeg"/></a>

The last talk was by open source rock-star aka Shakthi Kannan. His
talk was on "Pretty Printing in Python" i.e 3D printing using
python. He showed Prusa Mendel Hardware which he uses. Motivation of
talk was to build stuff by yourself without any need proprietary
software and hardware. He showed the SUPERMAN and BATMAN logo he built
with the printer. He quickly dived into the software he used for
giving instruction to printer. He pointed out the need for STL as end
goal for draw the object. Gcode is sent to arduino which handles the
further instructions. He then introduced suite for 3D printing like
"printrun" and "Skeinforge". He also mentioned "Blender" for 3D
modelling, Meshlab clould for real object and "pylatscan" for scanning
real objects and "rep rap" and "blenderpython".  He concluded his talk
with credits to people on Internet and his colleagues and interns who
helped him and mentions of IRC channels to get help from.

## Lightning Talks

Next up was for lightning talks, where Shakthi Kannan gave two
presentation where one consisted of 3d printing stuff. Another one was
awesome rhymes that are going to be prevalent to future software
developers.  Then I (Gaurav) gave a talk a talk on making reveal.js
slides using "Jupyter" aka "Ipython", without going through any
hassle.  Further Abhishek gave concerning talk about Volkswagen
scandal and how developers should be aware and be responsible of their
actions and code.

Then Vijay gave closing note of the meet-up with due gratitude to
sponsors, IMSc and participants. We then had a group photos which
concluded the evening with discussion.

Minutes contributed by <a
href="http://www.meetup.com/Chennaipy/members/73333582/">Gaurav
Sherawat</a>.