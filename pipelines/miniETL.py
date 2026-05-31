# ETL pipeline for employees data
import csv

from parso import python

data = "./Employees.csv"
# Extract

def extract(filepath):
    data_list = []
    with open(filepath , 'r') as file:
        reader = csv.DictReader(file)

        for read in reader:
            data_list.append(read)


    return data_list




# Transform


def transform(data1):
    cleaned_data = []

    for d in data1:
          if int(d["salary"]) > 40000:
              cleaned_data.append(d)


    return cleaned_data





# Load



def load(data , filepath):
    with open(filepath, 'w' , newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)




# functions call



Extracted =  extract(data)

Transform = transform(Extracted)

loaded =  load(Transform , "employees_clean.csv")

print(f"ETL pipeline ran successfully f{loaded}" )
