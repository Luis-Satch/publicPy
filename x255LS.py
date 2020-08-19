# RUN --> python3 x255LS.py WordCount.csv

# Objective: This script should do the following actions:
#  - (1) Read text from a given count.txt file
#  - (2) put the contents of count.txt in a list
#  - (3) Print the contents of the list
#  - (4) Save the content of the list as in .csv format

from sys import argv
import csv

#  - (1) Read text from a given WordCount.csv file
script, filename = argv

with open(filename, newline='') as csvfile:
    contents = csv.reader(csvfile)
#  - (2) put the contents of WordCount.csv in a list
    word_freq = []
    for freq, word in contents:
        word_freq.append((freq, word))
        print(f"{freq} {word}")
