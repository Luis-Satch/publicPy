# RUN --> python3 y254LS.py comments.txt

# Objective: This script should do the following actions:
#  - (1) Read text from a given .txt file
#  - (2) Clean the text, removing
#  - (3) Split the text into individual words
#  - (4) Count each word contained in the text file
#  - (5) Save results to a new file

# (1) Read text from a given .txt file
from sys import argv
script, textfile = argv

print("The file contains: ")
content = open(textfile, 'r')
mytext = content.read()
# print(f"{mytext} \n\n")

# (2) Clean the text, removing
for char in '-.,*/!$@#%^&*()_+=?:\'\"\n':
    mytext = mytext.replace(char,'')
mytext = mytext.lower()

# (3) Split the text into individual words
mytext = mytext.split(' ')
# print(f"{mytext}")

# (4) Count each word contained in the text file
d = {}

for word in mytext:
    d[word] = d.get(word, 0) + 1

word_freq = []
for key, value in d.items():
    word_freq.append((value, key))

word_freq.sort(reverse=True)
print(word_freq)

# (5) Save results to a new file
from os.path import exists
import csv

with open('WordCount.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['Freq','Word'])
    for row in word_freq:
        csv_out.writerow(row)


content.close()
