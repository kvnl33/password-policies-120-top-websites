#!/usr/bin/env python

#-----------------------------------------------------------------------
# myspacecom.py
# Author: Kevin Lee
#-----------------------------------------------------------------------

import re

#-----------------------------------------------------------------------

def myspace_passwordValidates(password):
    # (Reverse-engineered: 8 or more characters, 2 of: uppercase, lowercase, number, symbol)
    # Space doesn't count
    score = 0
    if len(password) >= 8:
        if re.match(r"^(?=.*[A-Z]).*$",password):
            score +=1
        if re.match(r"^(?=.*[a-z]).*$",password):
            score +=1
        if re.match(r"^(?=.*[\d]).*$",password):
            score +=1
        if re.match(r"^(?=.*[!\"#\$%&\'\(\)\*\+,\-\./:;<=>\?@\[\\\]\^_`{\|}~]).*$", password):
            score +=1
    return score >= 2
