import csv
import os
import pandas as pd
from pandas.io.common import EmptyDataError

os.chdir('C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT/reddit')
from pathlib import Path

wiki1="C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT/wiki_word_dataset.txt"
f1= open(wiki1,"a+")
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
print("DONE")

