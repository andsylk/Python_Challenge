#PyPoll

import os
import csv

#create candidates list
candidates = []


#read in csv file and append relevant column into list
with open('election_data_2.csv', newline = '') as file:
    election_data = csv.reader(file, delimiter = ',')
    next(election_data)
    for line in election_data:
        candidates.append(line[2])


#--------TOTAL VOTES (calc)
total_votes = len(candidates)
#print(total_votes)

#get the list of candidates
candidate_names = []
for x in candidates: 
    if x not in candidate_names:
        candidate_names.append(x)
    else:
        continue

#get each candidates votes and percentage of votes
candidate_votes = []
#Candidate 1
candidate1_votes = candidates.count(candidate_names[0])
candidate_votes.append(candidate1_votes)
candidate1_perc = round((candidate1_votes/total_votes)*100,2)
#print(candidate_names[0] + " has " + str(candidate1_votes) + " votes.")

#Candidate 2
candidate2_votes = candidates.count(candidate_names[1])
candidate_votes.append(candidate2_votes)
candidate2_perc = round((candidate2_votes/total_votes)*100,2)


#Candidate 3
candidate3_votes = candidates.count(candidate_names[2])
candidate_votes.append(candidate3_votes)
candidate3_perc = round((candidate3_votes/total_votes)*100,2)


#Candidate 4
candidate4_votes = candidates.count(candidate_names[3])
candidate_votes.append(candidate4_votes)
candidate4_perc = round((candidate4_votes/total_votes)*100,2)


#combine candidate names and candidate votes into dictionary
candidate_names_votes = {}
for i in range(len(candidate_names)):
    candidate_names_votes[candidate_names[i]] = candidate_votes[i]

#get the winning candidate
winning_candidate = max(candidate_names_votes, key=candidate_names_votes.get)



#---------SUMMARY OF RESULTS
print('')
print("Election Results")
print("-----------------------")
print("Total Votes: " + ": " +  str(total_votes))
print("-----------------------")
print(candidate_names[0] + ": " + str(candidate1_perc) + "% " + " (" + str(candidate1_votes) + ")" )
print(candidate_names[1] + ": " + str(candidate2_perc) + "% " + " (" + str(candidate2_votes) + ")" )
print(candidate_names[2] + ": " + str(candidate3_perc) + "% " + " (" + str(candidate3_votes) + ")" )
print(candidate_names[3] + ": " + str(candidate4_perc) + "% " + " (" + str(candidate4_votes) + ")" )
print("-----------------------")
print("Winner:  " + winning_candidate)
print("-----------------------")
print('')

#----------EXPORT RESULTS TO TEXT FILE
with open('poll_results.txt','w', newline = '') as outfile:
    print('', file = outfile)
    print("Election Results", file = outfile)
    print("-----------------------", file = outfile)
    print("Total Votes: " + ": " +  str(total_votes), file = outfile)
    print("-----------------------", file = outfile)
    print(candidate_names[0] + ": " + str(candidate1_perc) + "% " + " (" + str(candidate1_votes) + ")" , file = outfile)
    print(candidate_names[1] + ": " + str(candidate2_perc) + "% " + " (" + str(candidate2_votes) + ")" , file = outfile)
    print(candidate_names[2] + ": " + str(candidate3_perc) + "% " + " (" + str(candidate3_votes) + ")" , file = outfile)
    print(candidate_names[3] + ": " + str(candidate4_perc) + "% " + " (" + str(candidate4_votes) + ")" , file = outfile)
    print("-----------------------", file = outfile)
    print("Winner:  " + winning_candidate, file = outfile)
    print("-----------------------", file = outfile)
    print('')

