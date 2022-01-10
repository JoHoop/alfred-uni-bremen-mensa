#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import requests
import sys

MENSA_API_URL = 'https://api.mensa.legacymo.de/'

if __name__ == '__main__':
    response = requests.get(MENSA_API_URL)
    data = response.json()

    items = []
    for entry in data:
        for food in entry['food']:
            if not food['meal']:
                continue
            day = entry['day']
            dish = food['meal'][0]['name']
            cost = food['meal'][0]['costs']['a']
            type = food['type']
            if type.startswith('Cafe'):
                continue
            items.append({
                'title': dish,
                'subtitle': day + ', ' + cost + ' (' + type + ')',
                'autocomplete': dish,
                'icon': {'path': './icon.png'},
                })

    if not items:
        items.append({
            'title': 'No dishes found',
            'subtitle': 'Please try again later',
            'autocomplete': 'No dishes found',
            'icon': {'path': './icon.png'},
            })

    result = json.dumps({'items': items}, indent=2)
    sys.stdout.write(result)
