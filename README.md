# ProgressionOutcome
A program to predict progression outcomes at the end of each academic year of university students.

**CourseworkDescription**
---

A University requires a program to predict progression outcomes at the end of each academic year. You
should write this program in Python using the data shown below(passs, defer, fail, outcome).
  
1.  120   0   0 Progress
2.  100  20   0 Progress (module trailer)
3.  100   0  20 Progress (module trailer)
4.   80  40   0 Do not Progress – module retriever
5.   80  20  20 Do not Progress – module retriever
6.   80   0  40 Do not Progress – module retriever
7.   60  60   0 Do not progress – module retriever
8.   60  40  20 Do not progress – module retriever
9.   60  20  40 Do not progress – module retriever
10.  60   0  60 Do not progress – module retriever
11.  40  80   0 Do not progress – module retriever
12.  40  60  20 Do not progress – module retriever
13.  40  40  40 Do not progress – module retriever
14.  40  20  60 Do not progress – module retriever
15.  40   0  80 Exclude
16.  20 100   0 Do not progress – module retriever
17.  20  80  20 Do not progress – module retriever
18.  20  60  40 Do not progress – module retriever
19.  20  40  60 Do not progress – module retriever
20.  20  20  80 Exclude
21.  20   0 100 Exclude
22.   0 120   0 Do not progress – module retriever
23.   0 100  20 Do not progress – module retriever
24.   0  80  40 Do not progress – module retriever
25.   0  60  60 Do not progress – module retriever
26.   0  40  80 Exclude
27.   0  20 100 Exclude
28   0   0 120 Exclude
      
**Part 1 - Main Version**

- A. Outcomes
    - The program should allow students to predict their progression outcome at the end of each academic year. The
    program should prompt for the number of credits at pass, defer and fail and then display the appropriate
    progression outcome for an individual student (i.e., progress, trailing, module retriever or exclude).

- B. Validation
    - The program should display ‘Integer required’ if a credit input is the wrong data type.
    - The program should display ‘Out of range’ if credits entered are not in the range 0, 20, 40, 60, 80,
    100 and 120.
    - The program should display ‘Total incorrect’ if the total of the pass, defer and fail credits is not 120.
    - A few marks will be allocated for the efficient use of conditional statements. For example, the
    program does not need 28 condi􀆟onal statements for 28 outcomes.

- C. Multiple Outcomes
    - The program loops to allow a staff member to predict progression outcomes for multiple students.
    - The program should prompt for credits at pass, defer and fail and display the appropriate progression
    for each individual student until the staff member enters ‘q’ to quit. Optionally you can use an input of
    ‘y’ to continue.
    - See example of program run combined with Histogram below.

- D. Histogram
    - When ‘q’ is entered, the program should use the “graphics.py” module to produce a ‘histogram’
    represenring the number of students who achieved a progress outcome in each category range:
    progress, trailing, module retriever and exclude. The histogram should relate to the data input entered
    during the program run and work for any number of outcomes, it must use the graphics.py module.
    - Display the number of students for each progression category and the total number of students.
    - Example of a program run and input (in bold). Note: program should exit on ‘q’ to quit and produce the
    histogram. ‘y’ to con􀆟nue shown in the example is optional and depends on your program structure.

**Part 2 – List (extension)**

- For Part 1, most of the solutions would use variables to store the input data. For Part 2, extend your
solution so that the program saves the input progression data to a list or nested list. Then access the
stored data from the list and print the data in the following format below. Test plan not required.
Example Output: The following should display after the histogram

**Part 3 - Text File (extension)**
    
- For this part you could create an additional Part 3 program or extending your original version. Use
python to save any inputed progression data to a text file. Later in the program, access the stored
data and print out as shown below. Test plan not required.
