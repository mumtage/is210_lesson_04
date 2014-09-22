#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Versus"""

import data

MATCHUPS = ''
COUNTER = 0

for ROW_INDEX, ROW_NAME in enumerate(data.VERSUS):
    for COLUMN_INDEX, COLUMN_NAME in enumerate(data.VERSUS):
        if ROW_INDEX < COLUMN_INDEX:
            COUNTER += 1
            MATCHUPS += ('{0},"{1}","{2}"'.format(COUNTER, ROW_NAME, COLUMN_NAME))

print MATCHUPS
