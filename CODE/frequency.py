import nltk
import sys
import os

os.chdir('C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT')

with open ("wiki_word_dataset.txt", "r") as myfile:
    data=myfile.read().replace('\n', ' ')

data = data.split(' ')
fdist1 = nltk.FreqDist(data)
sys.stdout=open("frequency.txt","w")
print(fdist1.most_common())
sys.stdout.close()
