#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Versus"""

import data

MATCHUPS = ''
COUNTER = 0

for COLUMN_INDEX, COLUMN_NAME in enumerate(data.VERSUS):
    for ROW_INDEX, ROW_NAME in enumerate(data.VERSUS):
        if COLUMN_INDEX > ROW_INDEX:
            COUNTER += 1
            MATCHUPS += ('{0},"{1}","{2}"'.format(COUNTER, COLUMN_NAME, ROW_NAME) + "\n")

MATCHUPS = MATCHUPS.strip()

print MATCHUPS
