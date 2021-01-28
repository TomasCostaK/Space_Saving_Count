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
        final_tokens = []
        with open(self.file_path) as file:
            for lines in file:
                tokens = re.sub("[^0-9a-zA-Z]+"," ",lines).lower().split(" ")
                final_tokens.extend(token for token in tokens if len(token)>3)
        self.tokens.extend(final_tokens)

    def index(self):
        pass

    def addToken(self,token):
        self.word_dict[token] += 1


    def count(self):
        self.resetVars()
        self.tokenize()
        self.index()


class ExactCounter(Counter):
    def index(self):
        # treatment just for counter
        for token in self.tokens:
            self.addToken(token)
            self.counter_value += 1
        
        # calculate word_value
        self.word_counter += len(self.tokens)


class SpaceSavingCounter(Counter):
    def index(self):
        # treatment just for counter
        for token in self.tokens:
            self.addToken(token)
            self.counter_value += 1
        
        # calculate word_value
        self.word_counter += len(self.tokens)
