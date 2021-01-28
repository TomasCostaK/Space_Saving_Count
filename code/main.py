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
        elif o == "-t":
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
    counter_exact = ExactCounter(file_path)
    counter_exact.count()
    print(counter_exact.getCounter())
    exact_dict = counter_exact.getDict()

    # we calculate the values with space saving
    counter_space_saving = SpaceSavingCounter(file_path, epsilon)
    counter_space_saving.count()
    print(counter_space_saving.getCounter())
    space_saving_dict = counter_space_saving.getDict()
    """
    # Results analysis
    print(f"Executing {num_trials} trials on {epsilon} counter:\n")
    tic = time.time()
    trial_values = []
    for i in range(num_trials):
        counter.count()
        val = counter.getCount()
        trial_values.append(val)

    # evaluate only the last words into a dict
    top_words = counter.getTopWords(num_trials)

    toc = time.time()
    # We use NP to more efficiently calculate averages and std devs
    trial_values = np.array(trial_values)

    # Comparisons
    relative_errors_array = np.absolute(trial_values-real_value) / real_value
    max_re = np.max(relative_errors_array)
    min_re = np.min(relative_errors_array)
    mean_re = np.mean(relative_errors_array)


    # Print top words
    print("Ten most frequent words: (average)")
    print("Word \t\t Exact Count \t Avg. Est. Count \t Mean absolute error \t Mean relative error")
    print("----------------------------------------------------------------------------------------------------")
    for word in top_words:
        print(f"{word[0]} \t\t {exact_dict[word[0]]} \t\t {word[1]} \t\t\t {abs(word[1]-exact_dict[word[0]]):.1f} \t\t\t {abs(word[1]-exact_dict[word[0]])/ exact_dict[word[0]]*100:.2f}%")

    # Print out measures
    print("\nGlobal counter measures:")
    print(f"Maximum relative error: {max_re*100:.3f}%\nMinimum relative error: {min_re* 100:.3f}% \nMean relative error: {mean_re*100:.3f}%\n")
    

    print(f"Calculated in {toc-tic:.2f} seconds")
    # we dont go any further, this is the testing batch
    sys.exit()
    """
