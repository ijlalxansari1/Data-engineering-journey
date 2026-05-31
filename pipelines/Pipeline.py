import csv


file_csv = "Employees.csv"



def extract(filepath):
    data = []
    with open(filepath, "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
    return data



print(extract(file_csv))
