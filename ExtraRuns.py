import csv
from collections import defaultdict
file = open("matches.csv")
delivery = csv.DictReader(file)


runs = {}
runs["2016"] = {}
for match in delivery:
    year = match["season"]
    if str(year) == "2016":
        runs[year][match["winner"]] = runs[year].get(match["winner"],0) + int(match["win_by_runs"])
print(runs)
    


