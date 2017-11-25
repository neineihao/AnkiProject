# -*- coding: utf-8 -*-
import csv
from Lib import *
example = open('LOOKUPS.csv', 'r')

wordData = {}
with open('WORDS.csv', 'r') as words:
    spamreader = csv.reader(words, delimiter=',', quotechar='|')
    for i, row in enumerate(spamreader):
        if i == 0:
            continue
        # print("row: {}".format(row[0]))
        wordData[row[0]] = [row[1], row[2]]

with open('LOOKUPS.csv', 'r') as lookUp:
    spamreader = csv.reader(lookUp, delimiter=',', quotechar='|')
    for i, row in enumerate(spamreader):
        if i == 0:
            continue
        # print(', '.join(row))
        # print("key: {}".format(row[1]))
        # print("value: {}".format(row[5]))
        wordData[row[1]].append(row[5])

with open('./output.csv','a') as csvFile:
    csvApp = csv.writer(csvFile)
    # csvApp.writerow(['Expression', 'Meaning', 'Reading'])
    for key, value in wordData.items():
        # print(value)
        reading = value[0] + '[' + value[1] + ']'
        meaning = replaceWord(value[2], value[0])
        # print(reading)
        valueOutput = [value[0], meaning, reading]
        csvApp.writerow(valueOutput)

# print(wordData)


