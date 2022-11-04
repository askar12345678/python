import csv
import json
import os
import shutil
from os.path import expanduser
HOME = expanduser("~")

os.chdir(HOME)
if os.path.isdir('./hw3'):
    shutil.rmtree('./hw3')
os.mkdir('./hw3')
os.chdir('./hw3')


with open('file.txt', 'w') as file:
    file.write(
'''Do you believe in Heaven above?
   Do you believe in love?
   Don't tell a lie, don't be false or untrue
   It all comes back to you''')

    
data = {'movies': 
        [{'name': 'Полночь в Париже','release_year': 2011,'director': 'Вуди Аллен'},
         {'name': 'Гравити Фолз', 'release_year': 2012, 'creator': 'Алекс Хирш'},
         {'name': 'Окно во двор','release_year': 1954,'director': 'Альфред Хичкок'}]}

with open("file.json", "w", encoding='utf8') as out:
    json.dump(data, out, indent=4, ensure_ascii=False)

    
data1 = [
    ["Cancer Type","D-Loop","mRNAs","tRNAs","rRNAs","Nucleotide Position of Deletions","Increase of mtDNA copy #","Decrease of mtDNA copy #"],
    ["Bladder",1,1,0,1,"15642-15662",0,0],
    ["Breast",1,1,1,1,"8470-13447 and 8482-13459",0,1],
    ["Oral",1,1,0,0,"8470-13447 and 8482-13459",0,0]
        ]
with open("file.csv", "w") as file:
    writer = csv.writer(file)
    for row in data1:
        writer.writerow(row) 

        
os.chdir(HOME)
file_list = os.listdir('hw3')

for i in range(0, len(file_list)):
    file_list[i] = os.path.abspath('hw3/' + file_list[i])
    
print("Time of txt file creation :", os.stat('hw3/file.txt').st_mtime_ns)
print("Time of json file creation:", os.stat('hw3/file.json').st_mtime_ns)
print("Time of csv file creation:", os.stat('hw3/file.csv').st_mtime_ns)
time_sorted_file_list = sorted(file_list, key=lambda t: os.stat(t).st_mtime_ns)
print(time_sorted_file_list)

os.mkdir('./hw3/folder')
shutil.rmtree('./hw3')