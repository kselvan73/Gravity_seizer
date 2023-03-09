import re
import csv
import time
import psutil
# '''priogram starts'''
start_time=time.time()
# '''open the french_dictionary in read mode'''
# '''creating a otuput_dict with english word as key and french word as value (elements were taken from french_dictionary.csv file)'''
output_dict = {}
with open("french_dictionary.csv",'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        output_dict[row[0]]=row[1]
output_dict[header[0]] = header[1]
# ''' (input.file) read "original.txt" file line by line'''
# '''check for each output_dict key exist in each line'''
# ''' if exists replace themm using re.sub and update those line in "replaced_original.txt" (output.file)'''
f1 = open('t8.shakespeare.txt','r')
f2 = open('t8.shakespeare.translated.txt','w')
for line in f1:
    current_line =line
    for k,v in output_dict.items():
        current_line = re.sub(k, v, current_line)
    f2.write(current_line)
f1.close()
f2.close()
print("compeleted")
end_time = time.time()
time_taken_in_secs = end_time - start_time 
time_taken_in_mins=time_taken_in_secs//60
memory_taken = psutil.cpu_percent(time_taken_in_mins)
f = open("performance.txt", "w")
f.write(f'Time to process: {time_taken_in_mins} minutes\nMemory used: {memory_taken} MB')
f.close()









