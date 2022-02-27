from pdb import set_trace as debug
from pprint import pprint

categories={}

with open('completo.csv', 'r') as filein:
    for line in filein.readlines():
        splitted = line.split(',')
        ammount = float( splitted[3].replace('\"', '').replace('$', '') )
        if not splitted[1] in categories.keys() :
            categories[splitted[1]] = {'Detail':[ammount]}
        else:
            categories[splitted[1]]['Detail'].append(ammount)

for category in categories:
    categories[category]['Total'] = sum(categories.get(category).get('Detail', [0.999999]))

pprint(categories)
