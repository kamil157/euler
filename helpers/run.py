import sys
import os.path


def main():
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    for i in range(1, 40):
        exec("from tasks.task{i} import solve".format(i=i))
        eval("solve")()

if __name__ == '__main__':
    main()
