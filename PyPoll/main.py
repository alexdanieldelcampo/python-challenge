import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate_names = []
unique_list = []
candidate_votes = []

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    #this loop is for collecting total votes and setting up a list of candidate names to reduce later
    for row in csvreader:
       
        total_votes+=1
        candidate_names.append(row[2])
    
    # here I am creating a unique list of names
    for x in candidate_names:
        if x not in unique_list:
            unique_list.append(x)    
    # creating a list for candidate votes to match with the names
    for y in unique_list:
        
        candidate_votes.append(0)
    # needed to reset reader
    csvfile.seek(0)  
    next(csvreader)
    for row in csvreader:
        candidate_votes[unique_list.index(row[2])] += 1
        
analysis = '/Users/Alexander/DataClass/python-challenge/PyPoll/analysis/PyPoll_analysis.txt'
with open(analysis, 'w') as text:
    
    text.write('Election Results \n-------------------------')
    text.write(f'\nTotal Votes: {total_votes}')
    text.write('\n-------------------------')
    #here I used a 'for loop' to matchup the two lists
    for x in range(len(unique_list)):
        text.write(f'\n{unique_list[x]}: {round(candidate_votes[x]/total_votes*100, 4)}% ({candidate_votes[x]})')
 
    text.write('\n-------------------------')
    text.write(f'\nWinner: {unique_list[candidate_votes.index(max(candidate_votes))]}')
    text.write('\n-------------------------')