import csv
from collections import OrderedDict

def get_file(filename):
    with open(filename, 'r') as f:
        f = csv.DictReader(f)
        f = list(f)
        for i, d in enumerate(f):
            f[i] = dict(d)
        return f

data = get_file('moonbyte.csv')
for i, d in enumerate(data):
    d["red"] = int(d["red"], 16)
    d["green"] = int(d["green"], 16)
    d["blue"] = int(d["blue"], 16)
    data[i] = d

with open('moonbyte.csv', 'w') as f:
    fieldnames = ['name', 'x', 'y', 'z', 'visible', 'red', 'green', 'blue', 'type', 'dimensions']
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')

    writer.writeheader()
    writer.writerows(data)