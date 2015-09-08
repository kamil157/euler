def task79():
    with open("../res/task79_keylog.txt") as file:
        keys = [line for line in file.read().split()]

    guess = 73162890
    for key in keys:
        pos = [str(guess).find(c) for c in key]
        if pos != sorted(pos):
            print(key, "fail")
            return

    return guess


if __name__ == '__main__':
    print(task79())
