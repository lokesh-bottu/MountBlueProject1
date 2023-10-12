import csv
from collections import defaultdict
file = open("Deliveries.csv")
delivery = csv.DictReader(file)
cnt = 1
batsman_score = {}
for ball in delivery:
    if(ball["batting_team"] == "Royal Challengers Bangalore"):
        batsman_score[ball["batsman"]] = ball.get(ball["batsman"],0) + int(ball["total_runs"])
        print("over : ",ball["over"], ", Ball : ",ball["ball"]," Total Runs : ", ball["total_runs"],"  ",ball["batsman"])
        if cnt == 500:
            break
        else:
            cnt +=1
    else:
        pass
for i in batsman_score:
    print(i," : ",batsman_score[i])
        