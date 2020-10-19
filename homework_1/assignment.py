def a():
    first = 7
    second = 44.3

    print(first + second)
    print(first * second)
    print(second / first)


def b():
    a = 8
    a = 17
    a = 9
    b = 6
    c = a + b
    b = c + a
    b = 8

    print(a, b, c)


def c():
    pass
    print("The difference is using double or single quotes")
    print("The issue with the code is that we can't concatenate string and int, solution: use str()")


def d():
    print("It will print 7 since int(2.36) = 2")


def e():
    x = 432
    y = 231
    # One liner
    if x > y:
        print("BIG")
    elif x < y:
        print("small")


def f():
    my_number = 3
    if my_number == 1:
        print("summer")
    elif my_number == 2:
        print("winter")
    elif my_number == 3:
        print("fall")
    elif my_number == 4:
        print("spring")

    # Other option
    seasons = {
        1: 'summer',
        2: 'winter',
        3: 'fall',
        4: 'spring'
    }
    print(seasons[my_number])


def challenge():
    a = 8
    b = "123"

    # Instead of the following
    # print(a+b)

    # We can do
    print(a + int(b))
    # Or
    print(str(a) + b)


a()
b()
c()
d()
e()
f()
challenge()
