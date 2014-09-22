#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""meanwhile..."""

import data

ACCESS = False
PASSWORD = data.PASSWORD
COUNTER = 3

while not ACCESS:
    KEY = raw_input('Input the password? You have {0} attempts left : '.format(COUNTER))
    if KEY == PASSWORD:
        ACCESS == True
        print "ACCESS GRANTED"
    else:
        COUNTER -= 1
        if COUNTER == 0:
            print "TRY AGAIN SOME OTHER TIME"
            break
        
