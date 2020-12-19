# Create 2 vars with the value "5" and 5

five_str = "5"

five_int = 5

# Save the boolean result of the comparison of above vars
comparison = five_str == five_int

# Sum the two vars (Since will give error due to trying to add string with int, surround by try except)

try:
    my_sum = five_str + five_int
except:
    print("No way Jose")
