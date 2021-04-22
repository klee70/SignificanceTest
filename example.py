from art import *

def label_sequence_from_conll(fpath,gold=False):

    label_sequence = []

    with open(fpath,'rt',encoding='utf8') as f:
        lines = f.readlines()

        for line in lines:
            if line != '\n':
                if gold:
                    label = line.strip().split()[-2]
                else:
                    label = line.strip().split()[-1]

                label_sequence.append(label)

    return label_sequence


sys1_path = '../004_valid.txt'
sys2_path = '../051_valid.txt'

gold = label_sequence_from_conll(sys1_path, gold=True)
sys1 = label_sequence_from_conll(sys1_path, gold=False)
sys2 = label_sequence_from_conll(sys2_path, gold=False)

p_value = labelingsignificance(gold, sys1, sys2, N=9999)