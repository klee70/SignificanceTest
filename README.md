# SignificanceTest

import os
import sys
from art import *
 
sys1 = [<<<sequence of labels from system 1>>>]
sys2 = [<<<sequence of labels from system 2>>>]
gold = [<<<label from gold>>>]

p_value = labelingsignificance(gold, sys1, sys2, N=9999, verbose=False, training=None, scoring=getscores, common=common, common_gold=common_gold)

print(p_value)
