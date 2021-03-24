import os
import hashlib

os.chdir("C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT")


f1 = open("wiki_word_dataset.txt", 'r')

f2 = open("FINALOP.txt", 'w')
completed_lines_hash = set()

for w in f1:
    f2.write(w.rpartition("__")[0].replace("__", ".").replace("Wiki.","").replace("."," ").replace("_"," ").lower() + "\n")
f2.close()