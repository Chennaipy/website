Title: May 2017 Meetup Minutes
Date: 2017-05-27 15:30
Tags: Meeting Minutes


### Intro
Shrayas briefed the audience on the agenda of the meetup. He also went through what to expect from a meetup.

### Hadoop with Python by S.Venkatesh
It's a map reduce framework. Open source and maintained by Apache. Useful when text mining or performing LSA.

- File System
    - Stores files in folder
    - Chunk large files into blocks (64MB - 2GB)
    - 3 replicas of each block by default
    - Blocks are stored all over the system

- Map Reduce
    - Briefly went over what Mappers and Reducers are

- About the Hadoop System
    - Tools and languages that complement Hadoop
    - Similar competing tools

- Cool Things
    - Linear Scaling. Twice the number of data nodes results in twice the speed. Twice the amount of data doubles the time taken
    - Scheme on Read. Normally you'd have to specify the schema upfront. Hadoop allows great flexibility. Data is parsed when it is read. Multiple views of the same data
    - Transparent Parallelism. You don't have to deal with networking, locking and parsing issues
    - Unstructured Data. Media, text, logs etc. Also support structured data and SQL like language

- Mr Job
    - Python library for Hadoop
    - Open source, maintained by Yelp
    - Good support and documentation  

He then proceeded to show code samples

- Text Mining
    - Deriving high quality data text
    - Eg Amazon customer care reviews

- LSA
    - Latent Semantic Analysis. Try to establish relationships between words, group of words. Also tries to get the context and theme of the text.
    - Eg Panda in the text refers to the animal or the Python package

### Convolutional Neural Networks by Mohanraj V

- Introduction to Nerual Networks
    - Building blocks of deep learning systems
    - Mimics the human neuron
    - Input layer, hidden layer and output layer
    - Input layer is the size of the feature vector
    - Activation function. Each layer performs simple computations
    - Step function (the simplest activation function)
    - Fully connected networks

- Feed Forward
    - Can't go back during computation
    - Not used during training as it cannot improve itself
    - Showed an example network
    - Brief explanation about differences between feed forward and back propogation

He showed an example using Pima Indians Diabetes Dataset and Keras.

- General Info
    - [kaggle.com](kaggle.com) to improve skills and get job opportunities
    - [gogul09.github.io](gogul09.github.io) for articles on setting up and getting started with deep learning

- Convolutional Neural Networks
    - Convolution layer -> Taking kernel size and few other parameters
    - Pooling -> Data reduction layer
    - Fully connected networks

He then proceeded to show how to recognise digits from MNIST

### Networking and Tea Break by Qube Cinemas

### Deep Learning Based OCR Engine for Indus Scripts by Satish Palaniappan

- Where it all started?
    - How he got started? Stay away from the maths for a little while and a few other general tips
    - Showed a past project of his which built a little background in understanding this project

- Indus Scripts
    - Around 4000 years old
    - Not yet deciphered. Semantics unknown
    - He showed a few seals and characters and took the time to explain them

- Why are they still undeciphered?
    - Laborious
    - Very time consuming to standardise stuff
    - Political issues
    - Extremely old dataset (around 40  years old)

- Why deep learning?
    - 400+ characters in different variations
    - Semantics of the language are not known
    - Missing data

- Transfer Learning
Say you learn how to draw a bird, a face and an elephant with basic circles. You've actually mastered the skill of drawing circles. You're using that skill in different scenarios. Likewise neural networks to classify images start with classifying simple lines and dashes.  

He then went over the CNN architecture he used.

Procedure
- Extract seal. Smooth image to reduce cracks. Different techniques were used to ease the process of getting the seal
- Selective search
- Regional classification
- Text regional classification. Guessed areas where there might be text.
- Symbol segmentation. One it got an area which contains text, try extracting individual symbols.
- Symbol identification

### Lightning Talk #1 by Robin
Showed two handy one liners to deal with list of lists.

### Lightning Talk #2 by Sharmila
Shared a library called XMLToDict. Converts XML to Python list or dictionaries. Guarantees order in case of dictionary as well. It becomes easy to navigate as the dictionary order matches the XML.

### Lightning Talk #3 by Anish
Tips to stay healthy and energetic while coding at night. Use of Flux, light music and Vimperator.

### Lightning Talk #4 by Gaurav Sehrawat
Recommended Siraj Raval to familiarise yourself with new AI and ML related topics.

### Thanks
Venue and refreshments -> Qube Cinemas
