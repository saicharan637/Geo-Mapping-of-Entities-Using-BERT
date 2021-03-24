import spacy
import os


os.chdir("C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT")
nlp = spacy.load('en_core_web_sm') 

f1 = open('Final_Matching_Multiple_Words_with_BERT.txt','r')
f2 = open('analysis_multiple_word.txt', 'w')  
doc = nlp(f1.read()) 

for ent in doc.ents: 
    op1 = ent.text + '\n'
    op2=ent.label_ + ' '
    f2.write(op2)
    f2.write(op1)

f2.close()



"""
The Analysis is done based on the below table from spacy library:

TYPE    DESCRIPTION
PERSON  People, including fictional.
NORP    Nationalities or religious or political groups.
FAC Buildings, airports, highways, bridges, etc.
ORG Companies, agencies, institutions, etc.
GPE Countries, cities, states.
LOC Non-GPE locations, mountain ranges, bodies of water.
PRODUCT Objects, vehicles, foods, etc. (Not services.)
EVENT   Named hurricanes, battles, wars, sports events, etc.
WORK_OF_ART Titles of books, songs, etc.
LAW Named documents made into laws.
LANGUAGE    Any named language.
DATE    Absolute or relative dates or periods.
TIME    Times smaller than a day.
PERCENT Percentage, including ”%“.
MONEY   Monetary values, including unit.
QUANTITY    Measurements, as of weight or distance.
ORDINAL “first”, “second”, etc.
CARDINAL    Numerals that do not fall under another type

SORT the above data:

f1=open('analysis_multiple_word.txt','r')
f2=open("analysis_multiple_word_sort.txt",'w')
a=sorted(f1)
s=""
for i in a:
    s += i
f2.write(s)
f1.close()
f2.close()

"""