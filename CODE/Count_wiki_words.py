import os

os.chdir("C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT/reddit")
wiki_data = "C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT/wiki_word_dataset.txt"

count = len(open(wiki_data).readlines())
print("Total number of wiki words in the reddit dataset:", count)

