# python-challenge
Task 1. PyBank 
 a. In the PyBank assignment, I use list function in python to analyze PnL over months.
 b. first using csv reader to pull out all data in csv file 
 c. creating two lists that include date information and profit/loss numbers 
 d. -length reflects total months recorded 
    -sum all PL list to find net PL over the period
    -max and min functions to find the greatest increase and decrease amount in the list 
 e. then print out all information we just calculated by using f-strings
 f. finally write the output to a text file with wirte/close function in python


Task 2. PyRoll
The voting file contains a large amount of data. It would be easier and more efficient if we use pandas to analysis and calculate the numbers.

1. import pandas and os
2. use pandas to read the csv file
3. create data frames as needed
    - a data frame includes names only 
    - count values in the dataframe will reflect total votes 
    - use counts functions to find each candidate's votes 
    - create another data frame that contains all the results we just generated from the count function.
 4. use print function to display all results
 5. use write txt file function to export the results to a text file in analysis folder.
