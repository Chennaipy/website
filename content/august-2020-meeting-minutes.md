Title: August 2020 ChennaiPy Meetup - Meeting Minutes
Date: 2020-08-22 16:00
Tags: Meeting Minutes
Summary: The August 2020 ChennaiPy meetup featured talks on **Signal Processing with Python**, **Django web development**, **Flask rate limiting**, **Ray for distributed computing**, **Machine Learning for movie recommendations**, and more.

# ChennaiPy August 2020 Meetup - Meeting Minutes

The meetup took place on **August 22, 2020**, online due to the **Covid-19 pandemic**.

---

### Talk 1: Replacing MATLAB in Signal, Speech, Image and Video Processing
**Speaker:** Dr. Senthilkumar R

- **Python for Signal Processing**: Discussed how Python can replace MATLAB for signal, image, speech, and video processing.
- **Tools**: Covered **matplotlib**, **numpy**, **scipy**, **pillow**, and **opencv** modules.
- **Topics**: 
  - **Correlation algorithms** and **windowing techniques** for filter design.
  - **FIR filters** for signal processing.
  - **Image Processing**: Explained techniques in image processing using **opencv**.
  - **Video Processing** in **opencv**.
- **Examples**: Demonstrated various image processing applications.

---

### Talk 2: Discussing about a Web Project and the Issues I am Facing in It
**Speaker:** Lt Col CR Sundar

- Shared his experience in programming, starting with almost no programming knowledge and gradually improving over four years.
- Discussed issues faced while hosting a Django (Python) website and his decision to switch to PHP for a factory automation website.
- The session was disconnected before the speaker could demonstrate the issues on his website.

---

### Talk 3: Using Global Variables in Flask
**Speaker:** Rengaraj D

- **Flask App**: Developed a Flask app to get the IP address of client requests and restrict access if the same IP address requests within 60 seconds (rate limiting).
- **Problem**: The application faced issues when running with three processes using a global variable to track request times.
- **Proposed Solution**: Use **application or request context**, and either use a database or track session IDs instead of global variables.

---

### Talk 4: Intro to Ray, A Framework for Distributed Computing
**Speaker:** Krishna Sangeeth

- **Introduction**: Explained the evolution of computers from Babbage's machine to supercomputers.
- Discussed how **Moore's Law** is flattening and the need for distributed computing to solve computation power requirements.
- **Ray Framework**: Demonstrated how Ray can solve issues in distributed computing using a driver and individual workers.

---

### Talk 5: How I Will Be Using ML in My Movie Recommendation and Social Networking Website
**Speaker:** Sonam Pankaj

- **Classes of Learning Problems**: Explained her use of **unsupervised learning** for movie recommendations.
- **K-Means Algorithm**: Demonstrated how K-means can be used to classify data.
- Discussed **Expectation Maximization (EM)** algorithm and **dimensionality reduction** techniques.

---

### Talk 6: Floating Point Pitfalls
**Speaker:** Vijay Kumar

- **Floating Point Arithmetic**: Displayed sample Python code to demonstrate pitfalls in floating point arithmetic.
- **Binary Representation**: Discussed how fractional values are represented in binary and the algorithm to convert decimal to binary.
- **Avoiding Pitfalls**: Suggested using the **decimal class** in Python to avoid floating point errors.

---

### Talk 7: Three Good Reasons You Should Buy a Ticket to PyCon India
**Speaker:** Abishek Mishra

- **PyCon India**: Discussed the significance of **PyCon India** and this year's **online conference**.
- Explained the process of buying tickets and addressed doubts received through the chat.

---

### Talk 8: Test-Driven Teaching (TDT) in Python
**Speaker:** Ashok Bakthavathsalam

- **Introduction to TDT**: Explained how **Test-**
