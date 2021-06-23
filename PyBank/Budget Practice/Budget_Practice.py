import os 
import csv
#import os and csv modules
csvpath = os.path.join( "Resources", "budget_data.csv")
#create path to csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #read csv

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    #print column headers in csv file to terminal
    print("-----------------------------")
    data = []

    for row in csvreader:
        data.append(row)
        print(row)
    print("-----------------------------")
    # #loop through rows and print values to terminal

    dates=[]
    Prof_Loss=[]
    for row in data:
        dates.append(row[0])
        Prof_Loss.append(float(row[1]))
    print(dates)
    print("-----------------------------")
    print(Prof_Loss)
    print("-----------------------------")
    #create lists and print

    print(len(dates))
    print("-----------------------------")
    Net_Total= sum(Prof_Loss)
    print("$", sum(Prof_Loss))
    print("-----------------------------")
    #Net total of "Profit/Losses"

    changes=[]
    for x in range(1,len(dates)):
        change = Prof_Loss[x]-Prof_Loss[x-1]
        changes.append(change)

    avg_change=round(sum(changes)/len(changes),2)
    print(avg_change)
    print("-----------------------------")
    #Average of Changes in "Profit/Losses"


    max_change=max(changes)
    print(max_change)
    print("-----------------------------")
    #greatest increase in profits

    min_change=min(changes)
    print(min_change)
    print("-----------------------------")
    #greatest decrease in profits

    #print date to increase/decrease profits
    #print analysis and export text file with the results







