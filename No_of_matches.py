import csv
from collections import defaultdict
file = open("matches.csv")
delivery = csv.DictReader(file)

teams = {}
for match in delivery:
    year = match["season"]
    team1 = match["team1"]
    team2 = match["team2"]

    if year not in teams:
        teams[year] = {}
    yearkeys = list(teams[year].keys())


    if team1 not in yearkeys:
        teams[year][team1] = 1
    else:
        teams[year][team1] += 1

    if team2 not in yearkeys:
        teams[year][team2] = 1
    else:
        teams[year][team2] += 1
        
for i in teams:
    print(i," : ",teams[i])

