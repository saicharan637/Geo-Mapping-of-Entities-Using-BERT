import os
import csv
import sys
import nltk
import pandas as pd
import hashlib
from pandas.io.common import EmptyDataError
from pathlib import Path



# Counting Total number of words in the reddit data set

os.chdir("C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT/reddit")

word_count = 0
for fileName in Path('.').glob('*.txt'):
    with open(str(fileName.absolute()), 'r', encoding='utf-8') as f:
        for line in f:
            word = line.split()
            word_count += len(word)
print("Total number of words in the reddit dataset is", word_count)

#Extracting WIKI words from the data set

wiki1="C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT/wiki_word_dataset.txt"
f1= open(wiki1,"w")
for fileName in Path('.').glob('*.txt'):  
    lines = ""
    wikiword = ""
    with open(str(fileName.absolute()),'r',encoding="utf8") as one_text:
        lines=one_text.read()
        splitwords=lines.split(" ")    
        for i in splitwords:
            if (i.lower()).startswith("wiki_"):       
                wikiword=wikiword+i+"\n"
        f1.write(wikiword)
f1.close()
print("wiki_word_dataset has been created")

#Counting the total number of Wiki Words

wiki_data = "C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT/wiki_word_dataset.txt"
count = len(open(wiki_data).readlines())
print("Total number of wiki words in the dataset:", count)

os.chdir('C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT')

#Finding the Frequency of Every Wiki word

with open ("wiki_word_dataset.txt", "r") as myfile:
    data=myfile.read().replace('\n', ' ')

data = data.split(' ')
fdist1 = nltk.FreqDist(data)
sys.stdout=open("frequency.txt","w")
print(fdist1.most_common())

#Removing the Wikifier specific information at the beginning and at the end

f1=open("wiki_word_dataset.txt",'r')
f2=open("wiki_clean.txt",'w')

completed_lines_hash = set()

for w in f1:
    f2.write(w.rpartition("__")[0].replace("__", ".").replace("Wiki.","").replace("."," ").replace("_"," ").lower() + "\n")
f1.close()
f2.close()

# Frequency of Every Wiki Word after extracting the Wikifier specific information at the beginning and at the end

with open ("wiki_clean.txt", "r") as myfile1:
    data1=myfile1.read().replace('\n', ' ')

data1 = data1.split(' ')    
fdist2 = nltk.FreqDist(data1)
sys.stdout=open("wikiwords_frequency.txt","w")
print(fdist2.most_common())


#Removing the duplicate words in the file before comparing with BERT Vocab

output_file = open("OUTPUT.txt", "w")
f=open("wiki_clean.txt",'r')
for line in f:
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)

#Matching the WikiWords with BERT vocabulary and printing them to a new text file

file3 = open('Matching_with_BERT.txt','w')
file1 = set(line.strip() for line in open('OUTPUT.txt', 'r', encoding="utf8"))
file2 = set(line.strip() for line in open('BERT_Vocabulary.txt', 'r', encoding="utf8"))

for line in file1 & file2:

    if line:
        file3.write(line + "\n")

#List 1: only the wiki words that contain a one single word

a = open("OUTPUT.txt",'r')
b = open("single_words.txt",'w')

for i in a:
    for j in i:
        if j==" ":
            break
    if j!=" ":
        b.write(i)

#List 2: printing everything else into different lines because Bert expects only individual words

d = open('OUTPUT.txt','r')
c = open("multiple_words.txt",'w')

for i in d:
    for j in i.split():
        c.write(j)
        c.write('\n')


# Matching both the lists to BERT Vocab and printing the words which are there in BERT Vocab to a new text file

e = set(line.strip() for line in open('single_words.txt', 'r', encoding="utf8"))
match_single = open('Final_Matching_Single_Words_with_BERT.txt','w')


for line in e & file2:

    if line:
        match_single.write(line + "\n")


f = set(line.strip() for line in open('multiple_words.txt', 'r', encoding="utf8"))
match_multiple = open('Final_Matching_Multiple_Words_with_BERT.txt','w')


for line in f & file2:

    if line:
        match_multiple.write(line + "\n")


file3.close()        
sys.stdout.close()
a.close()
b.close()
c.close()
d.close()
match_single.close()
match_multiple.close()

