# BROKEN version
def broken(page, pages=[]):
    pages.append(page)
    return pages

print(broken(1))  # ?
print(broken(2))  # ?

print("---")

# FIXED version
def fixed(page, pages=None):
    if pages is None:
        pages = []
    pages.append(page)
    return pages

print(fixed(1))  # ?
print(fixed(2))  # ?