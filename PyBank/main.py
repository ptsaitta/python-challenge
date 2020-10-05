#modules#

import os
import csv


#set path to file

csvpath = os.path.join("../PyBank/", "Resources/", "budget_data.csv")

#read in datafile

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    csv_header = next(csvreader)
    
#Total Months portion

    monthcounter = 0

    for row in csvreader:
        monthcounter = monthcounter + 1

#total profit/loss

    profit = 0

    for row in csvreader:
        profit = profit + float(row[1])


    
#Average of the changes in "Profit/Losses" over the entire period

    averageprofit = 0

    averageprofit = profit/monthcounter
    

    biggestprofit = 0.0
    biggestprofitdate = ""

    
    for row in csvreader:
        if biggestprofit < float(row[1]):
            biggestprofit = float(row[1])
            biggestprofitdate = row[0]

    biggestloss = 0.0
    biggestlossdate = ""


    for row in csvreader:
        if biggestloss > float(row[1]):
            biggestloss = float(row[1])
            biggestlossdate = row[0]
    

#construct report

print("     Financial Analysis:")
print("--------------------------------")
print("Total Months: " + str(monthcounter))
print("Total Profit: " + str(profit))
print("Average Change: " + str(averageprofit))
print("Greatest Increase of Profits: " + biggestprofitdate + "; $" + str(biggestprofit))
print("Greatest Increase of Losses: " + biggestlossdate + "; $" + str(biggestloss))

#write report to output

f = open("../Reports/financialreport.txt", "w")
print("     Financial Analysis:", file=f)
print("Total Months: " + str(monthcounter), file=f)
print("Total: " + str(profit), file=f)
print("Average Change: " + str(averageprofit), file=f)
print("Greatest Increase of Profits: " + str(biggestprofitdate) + "; $" + str(biggestprofit), file=f)
print("Greatest Increase of Losses: " + str(biggestlossdate) + "; $" + str(biggestloss), file=f)
f.close()

#fin