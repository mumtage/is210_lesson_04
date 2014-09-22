#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""old bill"""

import data

print data.SHAKESPEARE

CRISPIAN = data.SHAKESPEARE.split('\n')
WORDS = 0
MAXIMUM_WORDS = 0
MINIMUM_WORDS = 0
AVERAGE_WORDS = float(0)
LINES = len(CRISPIAN)
NUM_CRISPIAN = 0

for line in CRISPIAN:
    if "Crispian" in line:
        NUM_CRISPIAN += 1
    for char in line:
        if char == ' ':
            WORDS += 1
    WORDS += 1
    AVERAGE_WORDS += WORDS
    if WORDS > MAXIMUM_WORDS:
        MAXIMUM_WORDS = WORDS
    elif WORDS < MINIMUM_WORDS or MINIMUM_WORDS == 0:
        MINIMUM_WORDS = WORDS
    WORDS = 0

AVERAGE_WORDS /= LINES

print (MAXIMUM_WORDS, MINIMUM_WORDS, AVERAGE_WORDS, NUM_CRISPIAN)
