import os
import csv


csvpath = os.path.join( "Resources", "budget_data.csv")

with open(csvpath) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    data = []
    for row in csvreader:
        data.append(row)

        
