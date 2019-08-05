import csv
import os
from collections import Counter

# Def totalMonths():
csvpath = os.path.join('..', 'HW 3', 'election_data.csv')
    
with open(csvpath, newline='') as csvfile:
    
 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    A= [] #list that will hold all of the votes
    
    #copies csv to a list
    for row in csvreader:
        A.append(row[2]) #adds votes

    vote_count = Counter()
    #created counter dictionary. if new key then adds it. if key exists increases count for that key by 1
    for word in A:
        vote_count[word]+=1
    # print(vote_count)
    
    total_votes = len(A)
   
    winner = vote_count.most_common(1)[0][0]

    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {total_votes}')
    print("-------------------------")
    for key, value in vote_count.items():
        percent = value/total_votes *100
        print(f'{key}: {"%.3f" % percent}% ({value})')
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")