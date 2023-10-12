import csv
from collections import defaultdict
file = open("Deliveries.csv")
delivery = csv.DictReader(file)
teams = {}
for ball in delivery:
    teams[ball["batting_team"]] = int(teams.get(ball["batting_team"],0)) + int(ball["total_runs"])
for i in teams:
    print(i," : ",teams[i])