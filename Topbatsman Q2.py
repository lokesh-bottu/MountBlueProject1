import matplotlib.pyplot as plt
import csv
from collections import defaultdict
file = open("Deliveries.csv")
delivery = csv.DictReader(file)
cnt = 1
batsman_score = {}
for ball in delivery:
    if(ball["batting_team"] == "Royal Challengers Bangalore"):
        batsman_score[ball["batsman"]] = batsman_score.get(ball["batsman"],0) + int(ball["total_runs"])


sorted_top_batsman= dict(sorted(batsman_score.items(), key=lambda item:item[1],reverse=True))
top10 = {}
cnt = 1

for i in sorted_top_batsman:
    top10[i] = sorted_top_batsman[i]
    if cnt == 10:
        break
    else:
        cnt +=1

for i in top10:
    print(i," : ",top10[i])

players = list(top10.keys())
rates = list(top10.values())

plt.bar(players, rates)
plt.xlabel('Batsman')
plt.ylabel('Runs Scored')
plt.title('Top 10 Batsman from RCB')
for i, rate in enumerate(rates):
    plt.text(i, rate, str(rate), ha='center', va='bottom')
plt.show()


