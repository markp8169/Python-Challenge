#PyPoll
import os
import csv

csvpath = os.path.join("election_data.csv")

# Total number of votes cast.
voterValue = 0
    
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    for row in csvreader:
        if row[0] != "string":
            voterValue += 1

# Complete list of candidates voted for
with open(csvpath, newline='') as csvfile:

    candidateList = csv.reader(csvfile, delimiter=',', skipinitialspace=True) 
    
    csv_header = next(candidateList)

    Candidate = []
    for row in candidateList:
        if row[2] not in Candidate:
            Candidate.append(row[2])  

# Total number of votes each candidate received.
khanVotes = 0
correyVotes = 0
liVotes = 0
tooleyVotes = 0
    
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        if row[2] == "Khan":
            khanVotes += 1
        elif row[2] == "Correy":
            correyVotes += 1
        elif row[2] == "Li":
            liVotes += 1
        elif row[2] == "O'Tooley":
            tooleyVotes += 1

#The percentage of votes each candidate won
khanPercent = (khanVotes / voterValue) * 100
correyPercent = (correyVotes / voterValue) * 100
liPercent = (liVotes / voterValue) * 100
tooleyPercent = (tooleyVotes / voterValue) * 100

#The winner of the election based on popular vote.
pollWinner = 0
winnerName = "String"

pollResults = [khanVotes, correyVotes, liVotes, tooleyVotes]

for number in pollResults:
    if (int(number) > int(pollWinner)):
        pollWinner = number

if (int(pollWinner) == int(khanVotes)):
    winnerName = "Khan"
    
elif (int(pollWinner) == int(correyVotes)):
    winnerName = "Correy"
    
elif (int(pollWinner) == int(liVotes)):
    winnerName = "Li"
    
elif (int(pollWinner) == int(tooleyVotes)):
    winnerName = "O'Tooley"

#Print election results
print("Election results")
print("-------------------------------")
print(f"Total votes: {voterValue}")
print("-------------------------------")
print(f"Khan:    {khanPercent}% ({khanVotes})")
print(f"Correy:  {correyPercent}% ({correyVotes})")
print(f"Li:      {liPercent}% ({liVotes})")
print(f"O'Tooley: {tooleyPercent}% ({tooleyVotes})")
print("-------------------------------")
print(f"Winner: {winnerName}")
print("-------------------------------")
#Output to text file
f = open('electionResults.txt','a')
f.write("Election results")
f.write('\n' + "-------------------------------")
f.write('\n' + f"Total votes: {voterValue}")
f.write('\n' + "-------------------------------")
f.write('\n' + f"Khan:    {khanPercent}% ({khanVotes})")
f.write('\n' + f"Correy:  {correyPercent}% ({correyVotes})")
f.write('\n' + f"Li:      {liPercent}% ({liVotes})")
f.write('\n' + f"O'Tooley: {tooleyPercent}% ({tooleyVotes})")
f.write('\n' + "-------------------------------")
f.write('\n' + f"Winner: {winnerName}")
f.write('\n' + "-------------------------------")
f.close()
