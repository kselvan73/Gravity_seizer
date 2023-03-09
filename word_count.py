# '''frequency of english word in original.txt files'''
import csv

# '''opening of french_dictionary.csv file in read mode '''
# '''updated the english word as key and french word as value'''
output_dict = {}
with open("french_dictionary.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        output_dict[row[0] ]  = row[1] 
# '''frequency count of word replaced''' 
field=["english_words","french_words","frequency"]   
f1 = open('original.txt', 'r')
word_freq_count=[]
file_data= f1.read()
for k,v in output_dict.items():
    occurrences = file_data.count(k)
    if occurrences!=0:
        word_freq_count.append([k,v,occurrences])     
# '''updating the frequency count in frequency.csv file'''
with open("frequency.csv", 'w',newline="") as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(["english_words","french_words","frequency"])
    for x in word_freq_count:
         csvwriter.writerow(x)