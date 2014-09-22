#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Teamwork"""

import data

PLAYERS = data.MULTIPLAYERS.split('\n')[1: len(data.MULTIPLAYERS)]
TEAM1 = ''
TEAM2 = ''
TEAM3 = ''
COUNTER = 0


for player in PLAYERS:
    NAME = ''
    for char in player:
        if char != ('1' or '0'):
            NAME += char
        elif char == '1':
            COUNTER += 1
            if COUNTER >= 13:
                break
            else:
                NAME = NAME.strip()
                TEAM = COUNTER % 3
                if TEAM == 1:
                    TEAM1 = TEAM1 + ',' + NAME
                elif TEAM == 2:
                    TEAM2 = TEAM2 + ',' + NAME
                elif TEAM == 0:
                    TEAM3 = TEAM3 + ',' + NAME

TEAM1 = TEAM1.lstrip(', ')
TEAM2 = TEAM2.lstrip(', ')
TEAM3 = TEAM3.lstrip(', ')

print TEAM1
print TEAM2
print TEAM3
