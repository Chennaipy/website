Title: May 2018 Meetup Minutes
Date: 2018-05-30 15:00
Tags: Meeting Minutes
Summary: <img src="https://secure.meetupstatic.com/photos/event/7/3/a/a/event_472109610.jpeg" alt=""/>

### Brief intro on the meetup by Vijay

The purpose of the meetup is to network with other python enthusiasts
and to get inspired by the various talks. The talks also provide some
exposure to the different facets of development and the various
problems that are being tackled. A meetup is not a workshop.

### Talk 1: How python is making astrophysical research easier

By Manjari Bagchi, Professor at IMSc

  * Used python for her research!!! Wants to generate interest in
    astrophysics. Studies cold dead stars that emit radio waves thanks
    to their magnetic fields
  
  * They are also known neutron stars - about 10 times heavier than
    the sun - very dense and regular gravitational physics cannot be
    used to explain their gravitational behavior? (not clear how they
    are different from black holes)

  * Require huge dishes to capture data. Uses python for data analysis

  * First encounter in 2010 - to analyze pulsar data
  
  * Was using unix command line utilities to do this - basically shell
    scripting. used the sigproc package developed by her mentor.
  
  * Popular library - astropy
  
  * There were some interesting asto terms that we were exposed to -
    right ascension, galactic center, declination etc

  * Showed a few examples -
  
    1. A file contained latitudes and longitudes of areas of interest
       which exhibited strong radio bursts. Python3 script to read
       this data and plot the positions on the globe - 3d earth image
       projects on to a 2d oval shaped earth on the screen. Used galpy
       for plotting(matplotlib?)

    2. Downloaded some data on a nebula captured by the Hubble
       telescope. Python script was used to plot this data.

    3. Astro plan - have the coordinate of most of the stars. Based on
       that and the longitude, latitude and time in a particular
       location this module will tell us if if that star is observable
       or not, rise time, set time and a trajectory

    4. galpy - a module for galactic dynamics


Call for contribution!!! Project SKA - Square Kilometer Array. Huge
sets of telescopes etc in Australia and South Africa are used to
capture data. Entire world is involved in this project. A lot of
programming is required for this. Those interested can contact her

Link to the National Center for Radio Astrophysics (also contains
links to the SKA Indian team???)
http://www.ncra.tifr.res.in/ncra/main

### Talk 2: Introduction to NLP & Spacy

By Vishal / Student @SSN

  * Natural Language Processing - parsing and mining information from
    natural language(as it is spoken or written)

  * 2 libraries in python - NLTK and Spacy NLTK - created in Stanford
    purely for educational purposes. Its only for English.

  * spaCy
    - Supports more than 28 languages
    - Much faster than NLTK. 
    - Developed for the industry
    - Uses a lot of memory (RAM)

  * Terms
    - Corpus - large data set for training and experimenting.
    - NLTK has a lot of built in corpora

  * Basic Pre-processing
    1. Convert everything to lower case.
    2. regex - to extract specific data out (remove dates from a text)
    3. Provision to handle special characters and encoding
    4. Tokenization break it down to chunks that can be processed 
    5. Stopword elimination

  * Language Based Pre-processing
    - POS - parts of speech - tagging each work as a noun/verb/ajective etc 
    - Stemming and lemmantization - get to the original word 
    - stemming -car cars, car's invariably mean car
    - lematizer - more useful, allows you to get words that do not
      have any common alphabets,but actually mean the same

  * Dived into code
    - An example of NLTK and spaCy were shown.

### Talk 3: Sultan and Errbot (last months lightning talk expanded upon)

By Samuel Vijaykumar (Freshworks)

   * Interacting with server via chat e.g Ask chatty? - what is the
     status of a particular build, current load on the server
   
   * ChatOps - currently used for managing infastructure. Devops
     through chatting -but not limited to it, usage limited by your
     imagination.

   * Before developing, requirements were
     - Conversational - not yet reached NLP
     - Operational - manage operations based on user rights and security
     - Extensible
     - Pythonic
     
   * Demo
     - create a slack channel, a plugin will allow you to execute your commands
     - errbot to create a bot.
     - sultan python library to ssh to servers and execute commands/
       also create agents that act on your behalf?
     - bot configuration
       1. BACK END - points to slack 
       2. BOT_IDENTITY - points to the slack channel?
 
### Lightning Talks

Lightning Talk by #Prasanth for microservices - lambda on aws and an
alternative project called pywren to help with scaling.

### Group Photo

<img src="https://secure.meetupstatic.com/photos/event/7/3/a/a/600_472109610.jpeg" alt="Group Photo"/></img>