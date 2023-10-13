import matplotlib.pyplot as plt
import csv
from collections import defaultdict
file = open("umpires.csv")
umpires = csv.DictReader(file)
umpire_country = {}
for person in umpires:
    country = person[" country"]
    if country != " India":
        umpire_country[country] = umpire_country.get(country,0)+1
    
for i in umpire_country:
    print(i," : ",umpire_country[i])



umpiress = list(umpire_country.keys())
count = list(umpire_country.values())
plt.bar(umpiress, count)
plt.xlabel('Umpires Country')
plt.ylabel('No of Umpires')
plt.title('Foreign Umpire Analysis')

plt.show()
