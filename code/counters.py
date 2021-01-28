import random
import math
import re
from collections import defaultdict 
import math

class Counter:
    def __init__(self, file_path):
        # Initialize array and declare file_path
        self.file_path = file_path
        self.tokens = []
        self.word_dict = defaultdict(lambda:  0)

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

    def addToken(self,token):
        self.word_dict[token] += 1

    def getCounter(self):
        return sum([ item for item in self.word_dict.values() ])

    def getDict(self):
        return self.word_dict

    def count(self):
        self.resetVars()
        self.tokenize()
        self.index()


class ExactCounter(Counter):
    def index(self):
        # treatment just for counter
        for token in self.tokens:
            self.addToken(token)


class SpaceSavingCounter(Counter):
    def __init__(self, file_path, epsilon):
        super().__init__(file_path)
        self.epsilon = epsilon

    def index(self):
        # treatment just for counter, this is acting as data_stream
        for token in self.tokens:
            self.addToken(token)