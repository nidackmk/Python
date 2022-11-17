import csv

with open('iris.data', newline='') as csvfile:
    print(csvfile)
    reader =csv.DictReader(csvfile)
    print(reader)

    for row in reader:
        print(row)

