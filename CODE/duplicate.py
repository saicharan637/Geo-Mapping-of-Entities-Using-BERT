import hashlib
import os

os.chdir('C:/Users/Sai Charan/Desktop/Studies/522-Advance_Data_Mining/PROJECT')

output_file_path = "OUTPUT.txt"
input_file_path = "FINALOP.txt"
#2
completed_lines_hash = set()
#3
output_file = open(output_file_path, "w")
#4
for line in open(input_file_path, "r"):
  #5
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  #6
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)


#7import sys

"""First of all, save the path of the input and output file paths in two variables. Change these values to your own input and output file path. You can drag and drop one file on the terminal to find out the path.
Create one Set variable. We are using Set because it can hold only unique variables. No duplicate variables can be added to a Set.
Open the output file in write mode. For opening a file in write mode, ‘w’ is used. We are opening the output file in write mode because we are going to write to this file. open() method is used to open a file.
Start one for loop to read from the input file line by line. We are opening the file in read mode. ‘r’ is used to read the file in read mode.
Find the hash value of the current line. We are removing any space and a new line from the end of the line before calculating the hash. hashlib library is used to find out the hash value of a line.
Check if this hash value is already in the Set variable or not. If not, it means the line is not printed to the output file yet. Put the line to the output file and add the hash value to the Set variable.
Finally, close the output text file."""