def add_numbers(num1, num2):
    result = num1 + num2
    return result


def add_space(str_1, str_2):
    result = str_1 + " " + str_2
    return result


# Test the add_numbers method

num_1_test = 7
num_2_test = 3

assert 10 == add_numbers(num_1_test, num_2_test)

# Test the add_space method

str_1_test = "Hello"
str_2_test = "World"

assert "Hello World" == add_space(str_1_test, str_2_test)
