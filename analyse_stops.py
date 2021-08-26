import csv

def load_source(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",")
        return list(reader)

sourcecsv = load_source("stops.txt")

for row in sourcecsv:
    if row[6] == "1":
        print(row)
