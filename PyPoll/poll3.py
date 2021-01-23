# import the modules I need
import os
import csv
# found this little gem https://docs.python.org/3/library/collections.html 
from collections import Counter

# honestly this was my part that I got stuck on for 3 HOURS
csvpath = os.path.join('Resources' , 'election_data.csv')

#appling my counter to get my total vote
vote_tally = Counter()

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # setting up which "column" of data I want my vote_tally to be
    for row in csvreader:
        vote_tally.update([row[2]])

# I want my total votes first before I can actually get the individual candidate total votes
total_votes = 0 
for candidate in vote_tally:
    total_votes += vote_tally[candidate]

# printing to get first requirement for challenge
print(f'Election Results')
print(f'---------------------------------')
print(f'Total Votes: {total_votes}')
print(f'---------------------------------')

# = "" sets a str or use stri()
# highest votes would be an integer and would start at zero
winner = ""
highest_vote = 0
for candidate in vote_tally:
    total_cand_votes = vote_tally[candidate]
    # here is where I can find the highest vote in my loop
    # if the total_cand_votes doesn't find to be higher, after it runs for each candidate, then this if statement won't be applied
    if total_cand_votes > highest_vote: 
        winner = candidate
        highest_vote = total_cand_votes
    print(f'{candidate}: {(total_cand_votes/total_votes):.3%} ({total_cand_votes})')
# I really don't like this fixed formating to my calculation because this isn't an accurate number, but it fixes it as shown in the homework example

print(f'Winner: {winner}')


pypoll_output = os.path.join("Analysis", "pypoll_output.txt")
with open(pypoll_output, "w") as new:
    new.write(f'Election Results\n')
    new.write(f'---------------------------------\n')
    new.write(f'Total Votes: {total_votes}\n')
    new.write(f'---------------------------------\n')
    new.write(f'Winner: {winner}\n')
