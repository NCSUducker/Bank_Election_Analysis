import os 
import csv
#import os and csv modules
#create path to csv file
csvpath = os.path.join( "Resources", "budget_data.csv")
txtpath = os.path.join( "Analysis", "Financial_Analysis.txt")

data = []
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    
    for row in csvreader:
        data.append(row)

#Months in dataset 
months = len(data)
# print(months)

#Net Profit/Loss
pandl = []
for row in data:
    pandl.append(int(row[1]))
total_pandl_ = sum(pandl)
# print(total_pandl_)

#avg change in profit/loss
changes = []
for i in range(1, len(pandl)):
    value = pandl[i]
    prev_value = pandl[i - 1]
    change = value - prev_value
    changes.append(change)
    # print(change)
    # print(changes)

avg_change = sum(changes)/len(changes)
# print(avg_change)

#Max Increase in profit/loss
max_change = max(changes)
print(max_change)
max_index = changes.index(max_change)
max_month = data[max_index + 1][0]
# print(max_month)

#Greatest decrease in profit/loss
min_change = min(changes)
print(min_change)
min_index = changes.index(min_change)
min_month = data[min_index + 1][0]
# print(min_month)

financial_analysis = f"""--------------------------------
Total months: {months}
Total P&L: ${round(total_pandl_, 2)}
Average change: ${round(avg_change, 2)}
Greatest Increase: {max_month} ({max_change})
Greatest Decrease: {max_month} ({min_change})"""




print (financial_analysis)
# print("--------------------------------")
# print(f"Total months: {months}")
# print(f"Total P&L: ${round(total_pandl_, 2)}")
# print(f"Average change: ${round(avg_change, 2)}")
# print(f"Greatest Increase: {max_month} ({max_change}")
# print(f"Greatest Decrease: {max_month} ({min_change}")

with open(txtpath, "w") as txtfile:
    txtfile.write(financial_analysis)