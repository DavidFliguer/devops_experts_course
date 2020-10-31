def ex_1_2():
    try:
        a = 1 / 0
    except ZeroDivisionError:
        print("Dividing by zero is only for the brave ones !!!")
