import tensorflow
import numpy as np
import os
import nltk
from nltk.corpus import stopwords
from pathlib import Path
from nltk.tokenize import word_tokenize
from bert_serving.client import BertClient

os.chdir('C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT/reddit')
nltk.download('stopwords')
bc = BertClient()
f2=open('BERT_Vocabulary.txt', 'r', encoding="utf8").readlines()
all_stopwords = stopwords.words('english')
os.chdir('C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT/reddit')
for fileName in Path('.').glob('*.txt'):
    a=str(fileName)
    lines=""
    wikiword=""
    f1=open("out.txt","a+")
    with open(str(fileName.absolute()),'r',encoding='utf-8') as one_text:
        lines=one_text.read()
        splitwords=lines.split(" ")
        for i in splitwords:
            if "wiki_" in i.lower():
                w=wikiword+i
                x=w.rpartition("__")[0].replace("__", ".").replace("Wiki.","").replace("."," ").replace("_"," ").lower() + '\n'
                for p in x:
                    if p==" ":
                        break
                if p!=" ":
                    if x not in all_stopwords:
                        if x in f2:
                            x=x.replace('\n','')
                            vec=bc.encode([x])
                            c=str(vec.argmax())
                            f1.write(a+','+x+','+c+'\n')
f1.close()
