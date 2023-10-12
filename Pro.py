import csv
from collections import defaultdict

file2 = open("matches.csv")
line = csv.DictReader(file2)


# def getheadings(lines):
#     for x in lines:
#         headings = list(x.keys())
#         break
#     return headings


# headings = getheadings(lines)






freq = []
key =[]
values =[]
dic ={}
# for i in lines:
#     for j in i:
#         headings.append(j)
#     break
# print(headings)




for k in line:
    key = list(k.keys())
    values  = list(k.values())
    break


for z in range(len(key)):
    dic[key[z]] = [values[z]]
# print(dic)


for k in line:
    siva = list(k.keys())
    lokesh  = list(k.values())
    for i in range(len(siva)):
        dic[siva[i]].append(lokesh[i])
#dictionary is created with all headings as keys and columns as values
print(dic["dl_applied"])