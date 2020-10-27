def get_number_from_user():
    user_number = input("Please enter a number")
    while not user_number.isdigit():
        user_number = input("Please enter again, we need a number")
    return int(user_number)


# This is a "mathematical" solution
def sum_digits_of_number(num):
    answer = 0
    while num > 0:
        i = 0
        while int(num / 10 ** i) >= 10:
            i = i + 1
        answer = answer + int(num / 10 ** i)
        num = int(num % 10 ** i)
    return answer


# Using a trick in order to iterate over the digits as a string and accumulating them as int
def sum_digits_of_number_version_2(num):
    answer = 0

    for digit in str(num):
        answer = answer + int(digit)

    return answer


# Some assertions to test (Not using input of user)

# First the one of the example
assert sum_digits_of_number(25) == 7

# Extra verification
assert sum_digits_of_number(25) == sum_digits_of_number(52)

assert sum_digits_of_number(1) == 1
assert sum_digits_of_number(2) == 2
assert sum_digits_of_number(12) == 3
assert sum_digits_of_number(120) == 3
assert sum_digits_of_number(1020) == 3
assert sum_digits_of_number(123) == 6
assert sum_digits_of_number(96) == 15

# First the one of the example
assert sum_digits_of_number_version_2(25) == 7

# Extra verification
assert sum_digits_of_number_version_2(25) == sum_digits_of_number_version_2(52)

assert sum_digits_of_number_version_2(1) == 1
assert sum_digits_of_number_version_2(2) == 2
assert sum_digits_of_number_version_2(12) == 3
assert sum_digits_of_number_version_2(120) == 3
assert sum_digits_of_number_version_2(1020) == 3
assert sum_digits_of_number_version_2(123) == 6
assert sum_digits_of_number_version_2(96) == 15
