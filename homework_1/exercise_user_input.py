name = input("Please, enter your name (Hope it starts with A...)")

# Check if name starts with A and if not, ask for it again
while not name.startswith("A"):
    name = input("Try again, need a name that starts with A...")

age = input("Please, enter your age")
work = input("Please, enter your work")

# Check if age is of type int (Since input is considered string it won't be)
if type(age) is int:
    print("Age is int")

# Check if age is number using isdigit

if age.isdigit():
    print("Age is digit")
