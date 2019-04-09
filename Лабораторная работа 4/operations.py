import numpy as np
import re
import string
import os
import hashlib
import sortedcontainers
from sortedcontainers import SortedDict
import pickle
import time
import hashlib

######################################################################
##################### Creating Hash From String ######################
######################################################################

def string2hash(text):
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:16], 16)



class RequestParser(object):
    pass

class SearchEngine(object):
    def __init__(self,represent = 1,**index:dict):
        if represent == 1:
            self.tree_dict = SortedDict()
            with open(index['tree_path'],'rb') as stream:
                self.tree_dict = pickle.load(stream)
        elif  represent == 2:
            with open(index['word_dictionary'],'rb') as stream:
                self.dict = pickle.load(stream)
            with open(index['coo_blocks'],'rb') as stream:
                self.coord_blocks = pickle.load(stream)
        else:
            raise RuntimeError
        
        