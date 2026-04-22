import csv


# Open and read the CSV file
with open("users.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)