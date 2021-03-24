import os

os.chdir("C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT")


file1 = set(line.strip() for line in open('OUTPUT.txt', 'r', encoding="utf8"))

file2 = set(line.strip() for line in open('BERT_Vocabulary.txt', 'r', encoding="utf8"))

file3 = open('Matching_with_BERT.txt','w')

for line in file1 & file2:

    if line:
        file3.write(line + "\n")
file3.close()        

