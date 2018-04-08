import pandas as pd
import numpy as np
from math import log
from DataLoader import DataLoader

[X,y,df] = DataLoader.getDataSet()

buildTree(X)

def buildTree(X) :
    print(X)