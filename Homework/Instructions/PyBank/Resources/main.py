#PyBank

import os
import csv

csvpath = os.path.join("budget_data.csv")

# Total number of months in dataset.
monthValue = 0
    
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        if row[0] != "string":
                monthValue += 1
                
monthValue -= 1
                
print(f"Number of months: {monthValue}")

# Total net amount of "Profit/Losses" over the entire period.
netProfit = 0
    
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    for row in csvreader:
        netProfit = netProfit + int(row[1])
        
print(f"Net profit: ${netProfit}")

# Average change in "Profit/Losses" between months, over the entire period.
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    firstRow = next(csvreader)

    for row in firstRow:
        firstValue = row
        
    for row in csvreader:
        lastValue = row[1]
        
averageChange = (int(firstValue) - int(lastValue)) / (int(monthValue) - 1)

print(f"Average Change: ${averageChange}")

# Greatest increase in profits (date/amount) over the entire period.
greatestDifference = 0
previousValue = 0

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    for row in csvreader:
        currentValue = int(row[1])
        
        valueDifference = (currentValue - previousValue)
        if (valueDifference > greatestDifference):
            greatestDifference = valueDifference
            differenceMonth = row[0]
        previousValue = int(row[1])
            
print(f"Greatest increase in profits: ${greatestDifference} on {differenceMonth}")

# Greatest decrease in losses (date and amount) over the entire period.
greatestLoss = 0
previousValue = 0

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    for row in csvreader:
        currentValue = int(row[1])
        
        valueDifference = (previousValue - currentValue)
        if (valueDifference > greatestLoss):
            greatestLoss = valueDifference
            lossMonth = row[0]
        previousValue = int(row[1])
        
greatestLoss = greatestLoss - (greatestLoss * 2)
            
print(f"Greatest decrease in profits: ${greatestLoss} on {lossMonth}")

#Write to .txt
f = open('bankResults.txt','a')
f.write("Financial Analysis")
f.write('\n' + "-------------------------")
f.write('\n' + f"Number of months: {monthValue}")
f.write('\n' + f"Total: ${netProfit}")
f.write('\n' + f"Average Change: ${averageChange}")
f.write('\n' + f"Greatest increase in Profits: ${greatestDifference} on {differenceMonth}")
f.write('\n' + f"Greatest decrease in profits: ${greatestLoss} on {lossMonth}")
f.close()
