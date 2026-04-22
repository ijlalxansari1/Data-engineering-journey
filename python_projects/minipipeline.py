import csv
from python_projects.Basic_de import clean_record



# step 1 read
with open("users.csv", "r") as file:
    reader = csv.DictReader(file)
    user_records = [row for row in reader]


# step 2 clean

cleaned_records= [clean_record(r)  for r in user_records ]



# Step 3 - WRITE
with open("cleaned_records.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "is_valid_age", "email", "country"])
    writer.writeheader()
    writer.writerows(cleaned_records)

print("Done! Check cleaned_records.csv")