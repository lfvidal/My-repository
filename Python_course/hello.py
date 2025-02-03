print("hello world")

picture = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
]


def show_umbrella():
    for row in picture:
        initialization = ""
        for value in row:
            if value == 1:
                initialization += "*"
            else:
                initialization += " "
        print(initialization)


show_umbrella()



