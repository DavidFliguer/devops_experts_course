def challenge_k():
    pyramid_len = 3
    for row in range(1, pyramid_len + 1):
        line_to_print = ""
        for columns in range(row):
            line_to_print = line_to_print + "*"
        print(line_to_print)


# A "pythonic" trick
def challenge_k_version_2():
    pyramid_len = 3
    for row in range(1, pyramid_len + 1):
        print("*" * row)
