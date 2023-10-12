import csv
from collections import defaultdict
file = open("matches.csv")
delivery = csv.DictReader(file)

teams = {}
for match in delivery:
    year = match["season"]
    winner = match["winner"]
    if year not in teams:
        teams[year] = {}

    if winner in teams[year]:
        teams[year][winner] += 1
    else:
        teams[year][winner] = 1

        
for i in teams:
    print(i," : ",teams[i])

