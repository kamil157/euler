import sys
import os.path


def main():
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    for i in range(1, 40):
        exec("from tasks.task{i} import task{i}".format(i=i))
        eval("task" + str(i))()

if __name__ == '__main__':
    main()
