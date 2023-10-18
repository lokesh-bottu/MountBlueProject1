import matplotlib.pyplot as plt
import csv
from collections import defaultdict
file = open("matches.csv")
delivery = csv.DictReader(file)

matches_played = {}
for match in delivery:
    year = match["season"]
    matches_played[year] = matches_played.get(year,0) + 1

    
for i in matches_played:
    
    print(i," : ",matches_played[i])

years = list(matches_played.keys())
no_of_matches = list(matches_played.values())

plt.bar(years, no_of_matches)
plt.xlabel('Year')
plt.ylabel('No of matched Played ')
plt.title('No of matches played per year for all years')
for i, no_of_matches in enumerate(no_of_matches):
    plt.text(i, no_of_matches, str(no_of_matches), ha='center', va='bottom')
plt.show()
