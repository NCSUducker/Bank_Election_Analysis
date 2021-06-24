import os 
import csv

path = os.path.join("Resources", "election_data.csv")
txtpath = os.path.join( "Analysis", "Poll_Analysis.txt")

with open(path) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    data = [row for row in csvreader]
    #copies rows out of csv reader


candidates = {}
#total votes
total_votes = len(data)
# print(total_votes)

#list of candidates, unique list using 'set' function
candidate_votes = []
for row in data:
    candidate_votes.append(row[2])

unique_candidates = set(candidate_votes)
# print(unique_candidates)

#key in candidates dic
for candidate in unique_candidates:
    candidates[candidate] = 0

#total voters per candidate
for vote in candidate_votes:
    candidates[vote] += 1
# print(candidates)

#vote percentage for each candidate
# candidates_pct = {}
# for candidate in unique_candidates:
#     vote_count = candidates[candidate]
#     candidates_pct[candidate] = int(round(vote_count/total_votes * 100, 0))


#winner
winner_name = ""
winner_votes = 0
winner_pct = 0 
for key, value in candidates.items():
    print(key, value)
    if value > winner_votes:
        winner_votes = value 
        winner_name = key 
        # winner_pct = candidates_pct[key]
# print(winner_name, winner_votes, winner_pct)
candidates_results = ""
for candidate in candidates: 
    # print(candidate)
    candidates_results = candidates_results + f'{candidate}: {round(candidates[candidate]*100/total_votes, 2)}% ({candidates[candidate]})\n'
# print(candidates_results)

election_results = f"""Election Results
------------------------------
Total Votes: {total_votes}
------------------------------
""" + candidates_results + f"""------------------------------
Election Winner: {winner_name}
"""

print(election_results)
with open(txtpath, "w") as txtfile:
    txtfile.write(election_results)

# #analysis print
# print("Election Results")
# print("---------------------")
# print(f"Total Votes: {total_votes}")
# print("---------------------")
# for w in sorted(candidates, key=candidates.get, reverse=True):
#     print(f"{w}: {candidates_pct[w]}% ({candidates[w]})"






