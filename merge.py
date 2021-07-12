import csv
import pandas as pd

d1 = []
d2 = []
with open("data.csv", 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d1.append(i)

with open("unit_converted_stars.csv", 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

p_d1 = d1[1:]
p_d2 = d2[1:]

h = h1+h2

p_d = []

for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)
with open("total_stars.csv", 'w', encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(p_d)

df = pd.read_csv('data.csv')
df.tail(8)
