#!/usr/bin/env python2
import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", help="JSON File from Trello", type=str)
parser.add_argument("output", help="File to output to", type=str)
parser.add_help = True
args = parser.parse_args()


print "Reading Data..."
with open(os.path.abspath(args.input)) as f:
    data = json.load(f)

print "Found {} cards in {} lists.".format(len(data['cards']), len(data['lists']))
print "Parsing..."

lists = {l['id']: l['name'] for l in data['lists']}
users = {u['id']: u['fullName'] for u in data['members']}
labels = {l['id']: l['name'] for l in data['labels']}

"""
parsed_cards = [{
    "name": c['name'],
    "list": lists[c['idList']],
    "description": c['desc'],
    "members": [u for k, u in users.items() if k in c['idMembers']],
    "labels": [l for k, l in labels.items() if k in c['idLabels']],
    "plugin": c['pluginData']
} for c in data['cards']]
"""
card = dict()
cards = tuple()

for c in data['cards'] :
    card = {'id' : c['id']}
    card.update({'list' : lists[c['idList']]})
    card.update({'desc' : c['desc']})
    card.update({'members': [u for k, u in users.items() if k in c['idMembers']]})
    card.update({"labels": [l for k, l in labels.items() if k in c['idLabels']]})

    # story point powerup data extract
    for p in c['pluginData'] :
        if 'value' in p :
            value = json.loads(p['value'])
            if 'points' in value :
                card.update({'point' : value['points']})
            else :
                card.update({'value' : p['value']})
        
    cards += (card,)

output = {
    "board_data": {
        "name": data['name'],
        "url": data['shortUrl']
    },
    "cards": cards
}

with open(os.path.abspath(args.output), 'w') as f:
    json.dump(output, f, indent=4)

print "Output to {} !s".format(os.path.abspath(args.output))
