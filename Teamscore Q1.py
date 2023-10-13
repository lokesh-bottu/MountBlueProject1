import matplotlib.pyplot as plt
import csv
from collections import defaultdict
file = open("Deliveries.csv")
delivery = csv.DictReader(file)
teams = {}
for ball in delivery:
    teams[ball["batting_team"]] = int(teams.get(ball["batting_team"],0)) + int(ball["total_runs"])

    
for i in teams:
    print(i," : ",teams[i])





batting_teams = list(teams.keys())
score = list(teams.values())
plt.bar(batting_teams,score)
plt.xlabel('Team')
plt.ylabel('Runs Scored')
plt.title("Runs Scored  by each Team")
plt.xticks(rotation=270)
for i, score in enumerate(score):
    plt.text(i, score, str(score), ha='center', va='bottom')
plt.show()
