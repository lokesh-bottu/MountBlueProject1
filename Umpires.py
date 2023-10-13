import csv
from collections import defaultdict
file = open("Deliveries.csv")
delivery = csv.DictReader(file)
umpires = {}
for ball in delivery:
    umpires[ball[""]] = int(teams.get(ball["batting_team"],0)) + int(ball["total_runs"])
for i in teams:
    print(i," : ",teams[i])