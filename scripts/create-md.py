import os
import csv

dir='/Users/nic/git/pf2e-monsters/'
filename = dir + 'monsters.csv'

if not os.path.exists(dir + '/monsterfiles'):
    os.makedirs(dir + '/monsterfiles')

monsterFilePath = dir + 'monsterfiles/'

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        name = row[0]
        size = row[1]
        level = row[2]
        keywords = row[3]
        hp = row[4]
        ac = row[5]
        tags = row[6]
        source = row[7]
        name = name.replace(',', ' -')
        name = name.replace('/', ' or ')
        print(name)
        with open(monsterFilePath + name + '.md', 'w') as output_file:
            string = f'''---
name: {name}
size: {size}
level: {level}
keywords: {keywords}
hp: {hp}
ac: {ac}
tags: {tags}
source: "{source}"
---'''
            output_file.write(string)
