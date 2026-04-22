


record = {
    "Full Name": "  john doe  ",
    "Age": 17,
    "Email": "JOHN@EXAMPLE.COM",
    "Country": "pakistan"
}


# dictionary manipulation



def is_valid_age(age):
    return 18 <= age <= 120


# Test it
record_new = {
    "Full Name": "  john caine  ",
    "Age": 18,
    "Email": "Caine@EXAMPLE.COM",
    "Country": "Norway"
}

def clean_record(record):

 return{
  "name": record["Full Name"].strip().lower(),
  "age": record["Age"],
  "is_valid_age": is_valid_age(int(record ["Age"])),
  "email" :record["Email"].strip().lower(),
  "country" : record["Country"].capitalize(),

}


# print(check_record(record_new))

# print(check_record(record))
