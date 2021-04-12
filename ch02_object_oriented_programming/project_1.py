# Created by Ellie Le at 4/11/2021

"""
Project problem: P-2.34

Write a Python program that inputs a document and then outputs a barchart plot
of the frequencies of each alphabet character that appears in that document.

"""
import collections
from collections import Counter
import matplotlib.pyplot as plt


fname = input('Enter the file name: ')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dict = {}
with open(fname) as f:
    for line in f:
        line = line.lower().strip()
        for word in line:
            word = word.split()
            for n in word:
                keys = dict.keys()
                if n in keys:
                    dict[n] += 1
                else:
                    dict[n] = 1

sortedDict = collections.OrderedDict(sorted(dict.items()))
print(sortedDict)

plt.bar(sortedDict.keys(),sortedDict.values())
plt.title('Frequencies of letter in ' + fname)
plt.xlabel('Letter')
plt.ylabel('Number of occurrences')
plt.show()



