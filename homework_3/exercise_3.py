def ex_3():
    try:
        x = 1
    finally:
        print("finally")

    # This code runs and executes the finally always, so it is legal
