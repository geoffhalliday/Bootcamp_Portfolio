# I have used 'file = open' rather than 'with open' to demonstrate the skill
# (I use 'with open' for the other task), but I would usually prefer to use 'with open'
# I reviewed the dataset to find relevant index numbers

file = open("DOB.txt","r")

lines = file.readlines()

# First name and surname are printed under the heading 'Name'
# Each line (x) is split (stored in y), and indices 0 (first name) and 1 (last name) are printed

print("Name")
for x in lines:
    y = x.split()
    print(f"{y[0]} {y[1]}")

# DOB is printed under the heading 'Birthdate'
# Each line (x) is split (stored in y), and indices 2 (day), 3 (month) and 4 (year) are printed

print ()
print("Birthdate")
for x in lines:
    y = x.split()
    print(f"{y[2]} {y[3]} {y[4]}")

file.close()
