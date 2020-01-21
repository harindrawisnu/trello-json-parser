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

print "Found {} cards in {} lists with {} actions.".format(len(data['cards']), len(data['lists']), len(data['actions']))
print "Parsing..."

users = {u['id']: u['fullName'] for u in data['members']}
# actions = {a['id']: a['data'] for a in data['actions']}

detail = dict()
parsed = tuple()
output = dict()

for a in data['actions'] :
    detail = {'actId' : a['id']}
    detail.update({'actType' : a['type']})
    detail.update({'board' : data['name']})
    if 'memberCreator' in a :
        detail.update({'actUser' : a['memberCreator']['fullName']})
    detail.update({'date' : a['date']})
    if 'list' in a['data'] :
        if 'name' in a['data']['list'] :
            detail.update({'list' : a['data']['list']['name']})
    elif 'listAfter' in a['data'] :
        detail.update({'list' : a['data']['listAfter']['name']})
    if 'card' in a['data'] :
        if 'id' in a['data']['card'] :
            detail.update({'cardId' : a['data']['card']['id']})
        if 'name' in a['data']['card'] :
            detail.update({'card' : a['data']['card']['name']})
    if 'text' in a['data'] :
        detail.update({'text' : a['data']['text']})
    parsed += (detail,)

output = parsed


with open(os.path.abspath(args.output), 'w') as f:
    json.dump(output, f, indent=4)

print "Output to {}!s".format(os.path.abspath(args.output))
