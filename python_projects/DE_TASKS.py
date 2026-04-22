from python_projects.Basic_de import check_record
from python_projects.Basic_de import is_valid_age
raw_records = [
    {"Full Name": "  john doe  ", "Age": 17, "Email": "JOHN@EXAMPLE.COM", "Country": "pakistan"},
    {"Full Name": "  john caine  ", "Age": 18, "Email": "Caine@EXAMPLE.COM", "Country": "Norway"},
    {"Full Name": "  sara khan  ", "Age": 25, "Email": "SARA@EXAMPLE.COM", "Country": "pakistan"},
    {"Full Name": "  bruce wayne  ", "Age": 35, "Email": "BRUCE@WAYNE.COM", "Country": "america"},
]

cleaned_records = [check_record(r) for r in raw_records]

for r in cleaned_records:
    print(r)