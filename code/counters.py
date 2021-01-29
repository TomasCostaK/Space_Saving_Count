import random
import math
import re
from collections import defaultdict 
import math
import sys

class Counter:
    def __init__(self, file_path, epsilon):
        # Initialize array and declare file_path
        self.file_path = file_path
        self.tokens = []
        self.word_dict = defaultdict(lambda:  0)
        self.epsilon = epsilon

    # Auxiliary function to help call multiple times
    def resetVars(self):
        self.tokens = []

    # Baseline function, all inherited classes will change this method, this is the method were we split into tokens
    def tokenize(self):
        with open(self.file_path) as file:
            for lines in file:
                tokens = re.sub("[^0-9a-zA-Z]+"," ",lines).lower().split(" ")
                self.tokens.extend(token for token in tokens if len(token)>3)

    def index(self):
        pass

    def getCounter(self):
        return sum([ item for item in self.word_dict.values() ])

    def getDistinctCounter(self):
        return len(self.word_dict.keys())

    def getDict(self):
        k = int(1/self.epsilon)
        #Always returns the top k words, as calculated by k=1/epsilon
        return sorted(self.word_dict.items(), key=lambda x: x[1], reverse=True)[:k]

    def count(self):
        self.resetVars()
        self.tokenize()
        self.index()


class ExactCounter(Counter):
    def index(self):
        # treatment just for counter
        for token in self.tokens:
            self.word_dict[token] += 1

class SpaceSavingCounter(Counter):

    def index(self):
        # treatment just for counter, this is acting as data_stream
        k = 1 / self.epsilon
        for token in self.tokens:
            #print("\nAnalyzing token: %s" % (token))
            # case for the token already in our dict
            if token in self.word_dict.keys():
                self.word_dict[token] += 1
            # case there is still space left in our dict
            elif len(self.word_dict.keys()) < k:
                self.word_dict[token] = 1
            # case where there is no space left, so we eliminate the smallest one and increment its counter with new "id"
            else:
                try:
                    ordered_dict = sorted(self.word_dict.items(), key=lambda x: x[1])
                    smallest_key, smallest_counter = ordered_dict[0]
                except:
                    sys.exit()
                #print(ordered_dict)
                #print("removing %s" % (smallest_key))
                self.word_dict.pop(smallest_key)
                self.word_dict[token] = smallest_counter + 1
