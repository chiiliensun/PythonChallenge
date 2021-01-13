import os
import csv

csvpath = os.path.join('election_data.csv')

candidates = []
votes = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])

total_votes = len(votes)
# print(total_votes)

#counting candidates' votes
Khan = candidates.count("Khan")
Correy = candidates.count("Correy")
Li = candidates.count("Li")
Otooley = candidates.count("O'Tooley")
# print(Khan)
# print(Correy)
# print(Li)
# print(Otooley)

# now for the candidates' percentages
# Khan_perc = (Khan/total_votes) * 100
# print(Khan_perc), need to round now 
Khan_perc = round(((Khan/total_votes) * 100), 5)
# print(Khan_perc) #I'm putting 5 digits to be safe
Correy_perc = round(((Correy/total_votes) * 100), 3)
Li_perc = round(((Li/total_votes) * 100), 5)
Otooley_perc = round(((Otooley/total_votes) * 100), 5)
# print(Correy_perc) I want to round more evenly, so I'm keeping this way
# print(Li_perc)
# print(Otooley_perc)

