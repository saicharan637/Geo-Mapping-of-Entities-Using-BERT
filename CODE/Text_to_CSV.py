import csv
import os
import pandas as pd
from pandas.io.common import EmptyDataError

os.chdir('C:/Users/Sai Charan/Desktop/data')
from pathlib import Path

with open('data.csv', 'w', encoding='utf-8') as out_file:
    csv_out = csv.writer(out_file)
    for fileName in Path('.').glob('*.txt'):
        lines = [ ]~
        with open(str(fileName.absolute()),'rb') as one_text:
            for line in one_text.readlines():
                lines.append(line.decode(encoding='utf-8',errors='ignore').strip())
        csv_out.writerow([str(fileName).join(lines)])

df = pd.read_csv('C:/Users/Sai Charan/Desktop/data/data.csv')
df.dropna(axis=0, how='all',inplace=True)
df.to_csv('new.csv', index=False)