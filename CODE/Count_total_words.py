import os

os.chdir("C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT/reddit")
from pathlib import Paths

word_count = 0
for fileName in Path('.').glob('*.txt'):
    with open(str(fileName.absolute()), 'r', encoding='utf-8') as f:
        for line in f:
            word = line.split()
            word_count += len(word)

print("Total number of words in the reddit dataset is", word_count)

