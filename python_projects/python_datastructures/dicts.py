# Raw customer records — messy, like real data
customers = [
    {"id": 1, "name": "Alice",    "email": "alice@example.com", "age": 30},
    {"id": 2, "name": "BOB",      "email": "bob@example.com",   "age": -5},  # bad age
    {"id": 3, "name": "Carol",    "email": "carol@example.com", "age": 25},
    {"id": 2, "name": "BOB",      "email": "bob@example.com",   "age": -5},  # duplicate!
    {"id": 4, "name": "",         "email": "ghost@example.com", "age": 40},  # missing name


]


# Step 1: Clean names (strip whitespace, fix casing)
for customer in customers:
    customer["name"] = customer["name"].strip().title()

def is_valid(record):
    """Returns True only if this record is worth keeping."""
    if not record["name"]:          # reject empty names
        return False
    if record["age"] < 0:           # reject impossible ages
        return False
    return True



