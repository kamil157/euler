def task63():
    return len(set(a ** b
                   for a in range(1, 10)
                   for b in range(100)
                   if len(str(a ** b)) == b))


def method_name():
    return


if __name__ == '__main__':
    print(task63())
