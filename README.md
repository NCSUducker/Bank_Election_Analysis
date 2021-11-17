# python-challenge
Python Project

## PyProjects

Welcome to python-challenge! In this project there are two parts, PyBank and PyPoll, that utilizes Python to create scripts to analyze the provided data. 

The objectives of the PyBank challenge are as follows:

*Analyze records to calculate* 
    
    -total # of months in the data set
   
    -Net total amount of "Profit/Losses" for the entire period
    
    -Average of the changes in "Profit/Losses" for the entire period
    
    -Greatest increase in profits over the entire period
    
    -Greatest decrease in losses over the entire period

In the main.py file created for the PyBank challenge, we begin by importing the 'os' and csv' modules in order to read in a path to the 'budget_data.csv' file and read the csv file itself.

Then we use a list comprehension technique to create a list for the variables and append the data to the list. 

Once this is complete we then create other list comprehensions and utilize our previous list to make calculations and analyze the data

The 'len' function is used to return the number of months in the data set 'data'

For Net Profit and Loss, the profits and losses are first appended to the second column in the list comprehension 'pandl' using a for loop. This column is then summed to arrive at the net profit and loss.

The average change calculation also uses list comprehension combined with a for loop to calculate the average change in the changes from each period. Once those changes(change) are calculated they are appended to the changes list. Average change is finally calculated by dividing the sum of changes by the number of changes
 
 (avg_change = sum(changes)/len(changes)

 The 'min' and 'max' functions in the 'changes' list to identiyf the max increase in profit/loss and the greatest decrease in profits/losses

 Finally we print our calculations to show a financial analysis of the calculations. This is done by using the 'f-string' technique and placing in the variables for the corresponding result

 The final step is writing code to pring the analysis to the terminal and export a text file with the results.

 This is accomplished by using the 'with' statement and writing the financial analylsis to a txt file.


The objectives of the PyPoll challenge are as follows:

*Analyze records to calculate* 
    
    -total # of votes cast
   
    -complete list of candidates who recieved votes
    
    -percentage of votes each candidate won
    
    -total number of votes each candidate won
    
    -winner of the election based on popular vote

This data is handled similarly to the PyBank challenge by creating scripts to allow calculations and manipulations

'len' function is used to calculate the total votes in the data set

'for' loops are utilized to append data to rows

looping through candidate votes after creating a dictionary key allows us to arrive at total voters per candidate

Using 'for' loops and conditionals allows winner's name, percent and votes to be calculated

These results are then populated using the 'f-string' function and keying in the variables for the values we want to display
