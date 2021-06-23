import os 
import csv

path = os.path.join("Resources", "election_data.csv")

with open(path) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    data = [row for row in csvreader]
    #copies rows out of csv reader


candidates = {}
#total votes
total_votes = len(data)
print(total_votes)

#list of candidates, unique list using 'set' function
candidate_votes = []
for row in data:
    candidate_votes.append(row[2])

unique_candidates = set(candidate_votes)
print(unique_candidates)

#key in candidates dic
for candidate in unique_candidates:
    candidates[candidate] = 0

#total voters per candidate
for vote in candidate_votes:
    candidates[vote] += 1
print(candidates)

#vote percentage for each candidate
candidates_pct = {}
for candidate in unique_candidates:
    vote_count = candidates[candidate]
    candidates_pct[candidate] = int(round(vote_count/total_votes * 100, 0))


#winner
winner_name = ""
winner_votes = 0
winner_pct = 0 
for key, value in candidates.items():
    if value > winner_votes:
        winner_votes = value 
        winner_name = key 
print(winner_name, winner_votes, winner_pct)




