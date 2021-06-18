import os 
import csv

csvpath = os.path.join( "Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)
#         #Create lists and print
# dates=[]
# Prof_loss=[]
# for row in csvreader:
#     dates.append(row[0])
#     Prof_loss.append(float(row[1]))
# print(dates)
# print(Prof_loss) 

# #Total Months
# print(len(dates))
# Net_Total= sum(Prof_loss)
# print("$", sum(Prof_loss))

# #Average Change
# changes=[]
# for x in range(1,len(dates)):
#     change = Prof_loss[x]-Prof_loss[x-1]
#     changes.append(change)

# #Greatest Increase
# maxchange=max(changes)
# print(maxchange)

# minchange=min(changes)
# print(minchange)
