; #-*- coding: utf-8 -*-
import csv
from Lib import *
example = open('LOOKUPS.csv', 'r')

wordData = {}
with open('SentenceData.csv', 'r') as words:
    spamreader = csv.reader(words, delimiter=',', quotechar='|')
    with open('./SentenceOut.csv', 'a') as csvFile:
        csvApp = csv.writer(csvFile)
        for row in spamreader:
            cloze = '{{c1::'+ row[1] + '::' + row[2] + '}}'
            # {{c1::1913}}.
            clozeCard = row[0].replace('＠', cloze)
            valueOutput = [clozeCard, row[3], '日語句型']
            csvApp.writerow(valueOutput)
