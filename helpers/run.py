import os.path
from os import listdir
from os.path import isfile, join


def main():
    files = (os.path.splitext(file)[0] for file in listdir('../tasks')
             if isfile(join('../tasks', file))
             if file.startswith("task"))

    for task in files:
        exec("from tasks.{} import solve".format(task))
        print(eval("solve")())


if __name__ == '__main__':
    main()
