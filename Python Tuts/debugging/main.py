def main():
    mario_bricks(8)


def mario_bricks(column):
    for i in range(column):
        print_space(column - i)
        print_row(i)


def print_space(n):
    for _ in range(n):
        print(" ", end="")


def print_row(row):
    print("#" * (row + 1))


main()
