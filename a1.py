# imports for sorting tuples (operator) and printing to cmd (sys)
import operator
import sys


def main():
    x = sys.argv[1]  # store file name from cmd
    f = open(x, "r")  # open file and store as f
    repeated = {}  # dictionary to store unique hex items and keep track of repetitions
    times = []  # Array to store final answer
    k = 1  # item repetition count default

    # parse through file and store unique hex items as int numbers in dictionary
    # while counting repetitions {item : repetitions}
    for i in f:
        if int(i.rstrip("\n"), 16) in repeated:
            repeated[int(i.rstrip("\n"), 16)] = repeated.get(int(i.rstrip("\n"), 16)) + 1
        else:
            repeated[int(i.rstrip("\n"), 16)] = k

            # sort dictionary by key value (unique items)
    sorted_x = sorted(repeated.items(), key=operator.itemgetter(0))

    # convert items back into hex form and store as strings in final array
    # drop items that do not repeat (with 1 in the second position of the tuple)
    for i in sorted_x:
        tolist = list(i)
        tolist[0] = str(hex(tolist[0])[2:]).rstrip("L")
        tolist[1] = str(tolist[1])
        if tolist[1] != "1":
            i = tuple(tolist)
            times.append(i)

    for i in times:
        print(i[0] + " " + i[1])


# call program
main()
