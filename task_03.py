#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Looper"""

import data

TRANS = data.TRANSACTIONS
DAY_TOT = 0
TOTAL = 0
MINIMUM = sum(trans[0])
MAXIMUM = 0

for day in TRANS:
    for t in day:
        DAY_TOT += t
        TOTAL += t
    if DAY_TOT > MAXIMUM:
        MAXIMUM = DAY_TOT
    elif DAY_TOT < MINIMUM:
        MINIMUM = DAY_TOT
    DAY_TOT = 0

print TOTAL, MINIMUM, MAXIMUM
