import os
import csv

csvpath = os.path.join( "Resources", "election_data.csv")

poll_dict = {}

rnum = 0 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        rnum += 1

        if row[2] in poll_dict:
            poll_dict[row[2]] += 1
        else:
            poll_dict[row[2]] = 1
    
    vote_total=rnum
    print("-----------------------------")

    print(f'Vote Totals: {vote_total}')
    print("-----------------------------")