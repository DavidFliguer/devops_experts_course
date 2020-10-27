def challenge_l():
    # As I see it, in order to have an X drawing as requested, width and length should always have the same value
    width = 3
    length = 3

    for x in range(length):
        index_of_stars = [x, width - x - 1]
        line_to_print = ''
        for y in range(width):
            if y in index_of_stars:
                line_to_print = line_to_print + "*"
            else:
                # In order to look like an X we might need spaces before and after each *
                line_to_print = line_to_print + " "
        print(line_to_print)
