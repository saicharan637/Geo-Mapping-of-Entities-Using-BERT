import os

os.chdir("C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT")

f1 = open("wiki_word_dataset.txt", 'r')

f2 = open("best.txt", 'w')

for w in f1:

    f2.write(w.replace("__", "."))
    


f1.close()
f2.close()

#for w in f1:
   # f2.write(w.replace("Wiki__","").lower())

   #f2.write(w.rpartition("__")[0] + "\n")
