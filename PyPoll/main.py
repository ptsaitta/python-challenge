#modules#

import os
import csv


#set path to file

csvpath = os.path.join("Resources", "election_data.csv")

#read in datafile

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    csv_header = next(csvreader)
    
#total number of votes cast


    votetotal = 0

    for row in csvreader:
        votetotal = votetotal + 1
    

#create list of all candidates who received votes

    candidates = []

    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])



#percentage of votes each candidate won
#Khan, Correy, Li, O'Tooley

    khanvotes = 0
    correyvotes = 0
    livotes = 0
    otooleyvotes = 0

    for row in csvreader:
        if row[2] == "Khan":
            khanvotes = khanvotes + 1
        elif row[2] == "Correy":
            correyvotes = correyvotes + 1
        elif row[2] == "Li":
            livotes = livotes + 1
        else: otooleyvotes = otooleyvotes + 1

    khanpercent = khanvotes/votetotal * 100
    correypercent = correyvotes/votetotal * 100
    lipercent = livotes/votetotal * 100
    otooleypercent = otooleyvotes/votetotal * 100

    winner = ""

    if khanpercent > correypercent and khanpercent > lipercent and khanpercent > otooleypercent:
    winner = "Khan"
    
    elif correypercent > lipercent and correypercent > otooleypercent:
    winner = "Correy"

    elif lipercent > otooleypercent:
    winner = "Li"

    else: winner = "O'Tooley"


#construct report

print("     Electoral Results:")
print("-----------------------------")
print("Total Votes: " + str(votetotal))
print("-----------------------------")
print("Khan: " + str(khanpercent) + "%")
print("Correy: " + str(correypercent) + "%")
print("Li: " + str(lipercent) + "%")
print("O'Tooley: " + str(otooleypercent) + "%")
print("-----------------------------")
print("Winner: " + winner)
print("-----------------------------")
    
#write report to output

f = open("../Reports/electionresults.txt", "w")
print("     Electoral Results:", file=f)
print("-----------------------------", file=f)
print("Total Votes: " + str(votetotal), file=f)
print("-----------------------------", file=f)
print("Khan: " + str(khanpercent) + "%", file=f)
print("Correy: " + str(correypercent) + "%", file=f)
print("Li: " + str(lipercent) + "%", file=f)
print("O'Tooley: " + str(otooleypercent) + "%", file=f)
print("-----------------------------", file=f,)
print("Winner " + winner, file=f)
print("-----------------------------", file=f)
f.close()

#fin