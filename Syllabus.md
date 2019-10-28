# COMP 205 &mdash; Principles of Data Science in Python


## Course at a glance

* **Instructor** Jitendra Singh
    - Email: [Jitendra.Singh@tufts.edu](Jitendra.Singh@tufts.edu)
    - Phone: +1 (617) 444-9640
* **TA** Amanda N. Rodriguez
    - Email: [arodri12@tufts.edu](arodri12@tufts.edu)
* **Textbooks** While there is no assigned textbook, if you are new to Python, there are many appropriate introductions to the language, including print books and online tutorials. For the later parts of the course, we will use [Python Data Science Handbook](http://shop.oreilly.com/product/0636920034919.do) by Jake VanderPlas &copy; 2017, O'Reilly Media.
* **Prerequisites**
    - Two semesters of college mathematics (e.g., Calculus 1 and 2).
    - Ability to write a simple program in some high-level language will help considerably (e.g., C, C++, Java, Python, Basic, etc).
* **Grading Rubric**
    - Weekly online exercises (65% of course grade)
    - Online midterm and final exams (15% and 20% of course grade)
* **Communication** There are different venues for bringing questions outside the lecture hours:
    1. First, please utilize the discussion boards on Canvas - as it is monitored daily. Plus other students could likely benefit from the Q & A. Some students may answer your questions even faster! 
    2. If you need to get in touch with the TA/instructor, for example to set up a meeting or ask a question unrelated to course content, feel free to _use Canvas to email_ them.
    3. If no response from (i) or (ii) within 24 hrs, or **in case of an emergency, please call the instructor**.

## Overview

_Getting analysis results is the easy part. The hard part is showing others how you got there and convincing them!_

COMP-205 is intended as a first course in programming for those studying toward the Master of Science in Data Science and related degrees, including engineering Master of Science degrees with an emphasis upon data analysis.
The perspective this course takes on data analysis is that data analysis is a social activity, and that human communication is as important as analysis skills. Thus, in our program, we emphasize not just analysis, but also communicating results to others in a manner that allows reproduction of results and critical analysis. One of the most powerful tools we have is literate programming in which an interpretation of program results is presented alongside the program itself. Thus, another researcher can view both your analysis methods and your conclusions and evaluate whether those make sense together.

There is increased emphasis on not only publishing interesting results but also publishing exactly how those results were obtained. Jupyter notebooks permit researchers to publish not only the raw data they obtained in their research but also the calculations that led to their conclusions, making it possible for other researchers to replicate the analysis and try alternative analses. Jupyter [a compound of Julia, Python and R, though it actually supports many data science languages in addition to those three] serves the need for repeatable data science analyses. One of the most popular languages for undertaking data analysis is Python, and thus Python-on-Jupyter is becoming one of the more popular frameworks for Data Science.

The framework is based on Jupyter Notebooks. Jupyter can be run on any kind of computer and online via the "Jupyter Hub" framework, and enables literate programming, in the sense that one can create "notebooks" that contain programs, visual results, and commentary in English. Jupyter Notebooks have become the lingua franca of data analysis. They can be created, saved, mailed to others, and modified and executed again by those who receive them. Thus, we are not just employing a computer language, but also a powerful collaboration model for sharing critical analyses and repeating experiments of others.

Using Jupyter Notebooks and Python 3, this course concentrates upon the programming tasks often required for phase 1, with examples of phases 2 and 3, which will be covered in more depth in later courses. Very often, significant programming is required in order to make data ready for analysis. We will cover several common programming tasks that one might need to complete during the data analysis lifecycle, mostly centered upon preparation of data collected and published by others, with the intent of running data analysis functions written by yet another group of people. Differences in how people approach data collection and analysis make this kind of programming a common need in data science.

| Wk  |  M  |  W   | Topic  | Notebooks |
| :---: | :---: | :----: | :------ | :----- |
|  8  |  10/22  | 24  | **Numpy:** Reading into multi-dimensional arrays, **Pandas:** Dataframes and reading into them  | 03-03, 03-04 |
|  9  |  29  | 31  | **Pandas:** Merging and matching Dataframes, Series and Views| 03-05, 03-06, 04-01 |
|  10 |  11/4   | 6   | Classification and Clustering | 04-02, 04-03 |
|  11 |  11  | 13  | **Case Study:** [World Happiness Report](https://worldhappiness.report/ed/2019/)  | 04-04, 05-01 |
|  12 |  18  | 20  | **Matplotlib**  | 04-06, 04-07 |
|  13 |  25   | &mdash;  | **Case Study:** World Happiness Map | 05-03 |
|  14 |  12/2 | 4 |  **Case Study:** Twitter Sentiment Analysis | 05-04 |
|  16 |  | 12/13 | **(Take Home) Final Exam**  |



COMP-205 loosely follows the Data Processing Pipeline.
![Data Processing Pipeline](https://s3.amazonaws.com/libapps/accounts/95901/images/data_processing_pipeline.JPG)
credit: Martin Magdinier, University of Texas.

**Module 1** sweeps through some of the basic concepts on which this course is based. 
**Module 2** is an introduction to Python as a programming language. It skips some [advanced features of Python](https://scipy-lectures.org/advanced/advanced_python/index.html) that may be of interest in an advanced Python programming course.
**Module 3** builds on Module 2 to help develop the skills at which data scientists spend a bulk of their time professionally.
**Module 4** covers analysis and visualization, which is the goal of data science: to draw actionable conclusions.

## History
* Original Jupyter Notebooks for the course in Summer 2019, by Prof. Alva Couch.
* Adapted for Fall 2019 by Jitendra Singh.
* Last updated 9/9/19
