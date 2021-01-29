from counters import *
import sys
import getopt
import random
import time
import os.path
import numpy as np

def usage():
    print("Usage: python3 main.py \t(Please provide an epsilon and a file path)\n\t-e,  <real>\t<type of probabilistic counter>\n\t-f,  file_path\t\t<File used for reading>")

if __name__ == "__main__":
    # initialization of random variables
    epsilon = 0.2
    file_path = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "he:f:", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    temp_opts = [x[0] for x in opts]
    if "-e" not in temp_opts or "-f" not in temp_opts:
        usage()
        sys.exit(1)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o == "-e":
            try:
                epsilon = float(a)
            except Exception:
                print("Provide a real number as epsilon")
                usage()
                sys.exit()
        elif o == "-f":
            if os.path.isfile(a):
                file_path = a
            else:
                print ("File does not exist")
                usage()
                sys.exit()


    # we calculate exact values to compare afterwards
    counter_exact = ExactCounter(file_path, epsilon)
    counter_exact.count()
    print("# Words\nExact Count:\t\t", counter_exact.getCounter())
    exact_dict = counter_exact.getDict()
    #print(exact_dict)

    # we calculate the values with space saving
    counter_space_saving = SpaceSavingCounter(file_path, epsilon)
    counter_space_saving.count()
    print("Space Saving Count:\t", counter_space_saving.getCounter())
    space_dict = counter_space_saving.getDict()
    #print(space_dict)

    # Get Distinct Counters
    print("\n# Distinct Words\nExact Distinct Count:\t\t", counter_exact.getDistinctCounter())
    print("Space saving Distinct Count:\t", counter_space_saving.getDistinctCounter())

    # Results analysis
    exact_array = [ item[0] for item in exact_dict]
    space_array = [ item[0] for item in space_dict]
    
    length = len(exact_dict)
    accuracy = len(list(filter(lambda x: x in exact_array, space_array))) / length
    print("\nAccuracy of the %d most frequent words is: %.2f " % (length, accuracy*100))