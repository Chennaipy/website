Title: Meeting Minutes of 6/27/2020 ChennaiPy
Date: 2020-06-27 16:00
Tags: Meeting Minutes
Summary: The June 2020 ChennaiPy meetup included talks on **Role of Python in ETL**, **Cyclic Redundancy Check (CRC)**, and several open slots with interesting suggestions.

# ChennaiPy June 2020 Meetup - Meeting Minutes

The meetup took place on **June 27, 2020**, at **Chennai**.

---

### Talk 1: Role of Python in ETL
**Speaker:** Deepak

- **ETL** (Extract, Transform, Load) - Python’s role in customizing ETL workflows due to its readability and ease of use.
- **Python ETL Tools**:
  - **Petl**: Example with converting a 4x2 array to HTML.
  - **Pandas**: ETL with transformations and conditions.
  - **Mara**: Lightweight, web-based UI.
  - **Apache Airflow**: Created by Airbnb, uses DAGs (Directed Acyclic Graphs).
  - **Pyspark**: Big data tool for data streaming and ML on top of streaming data.
  - **Bonobo**: Supports parallel processing.
  - **Luigi**: Created by Spotify, designed for enterprise-level solutions with increasing data.
  - **AVIK Cloud**: Not open source, but Python can be implemented directly.

**Q&A**:
- **Ashok**: "Can you explain the pipeline?"
- **Deepak**: "For enterprise-level activities, multiple parallel operations are handled by creating pipelines."

---

### Talk 2: Introduction to Cyclic Redundancy Check (CRC)
**Speaker:** Ashok

- **Cyclic Redundancy Check (CRC)** is used for error detection in computer networks.
- **Types of Errors**:
  - **Single Bit Error**
  - **Burst Error**
- **Error Detection**: Adding redundancy bits to transmitted data.
  - Example: Transmitting 1000 bits from CP1 to CP2 with 125 redundancy bits.
  - **State Machine** and **2-Dimensional Parity Check**.
  - **Checksum**: Binary Addition.
- **CRC Computation**: Performed using XOR in polynomial division.
  
**Conclusion**: CRC errors can occur when accessing the hard drive.

---

### Open Slot

- **Ashok**: Suggested documentaries available on Netflix:
  - **"Prediction by the Numbers"**
  - **"The Code"** (3 episodes).
  - Context: They provide real-life connections to mathematical concepts, like Bayes' theorem and fractals.
  
- **Rengaraj**: Announcement for **PyCon India 2020**.
  
- **Pradeep**: Suggested resources from **MIT OpenCourseWare**: [MIT OpenCourseware](https://ocw.mit.edu/index.htm).
  
- **Vijay Ravider**: Talked about **Python modules used in infrastructure-based provisioning services**.

---

The meetup concluded with a lively discussion and networking.

Meeting minutes contributed by
