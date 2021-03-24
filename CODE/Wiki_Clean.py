import os

os.chdir('C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT')
f1=open("wiki_word_dataset.txt",'r')
f2=open("wiki_clean.txt",'w')
for w in f1:
    f2.write(w.split("__")[1].replace("_"," ").lower()+'\n')
f1.close()
f2.close()