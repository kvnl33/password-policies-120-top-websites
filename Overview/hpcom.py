#!/usr/bin/env python

#-----------------------------------------------------------------------
# hpcom.py
# Author: Kevin Lee
#-----------------------------------------------------------------------

import re

#-----------------------------------------------------------------------

def hp_passwordValidates(password):
    # 8 characters minimum required3 of the following required
    # 1 uppercase letter1 lowercase letter1 number (0-9)1 special character
    score = 0
    if len(password) >= 8:
        if re.match(r"^(?=.*[A-Z]).*$",password):
            score +=1
        if re.match(r"^(?=.*[a-z]).*$",password):
            score +=1
        if re.match(r"^(?=.*[\d]).*$",password):
            score +=1
        if re.match(r"^(?=.*[\s!\"#\$%&\'\(\)\*\+,\-\./:;<=>\?@\[\\\]\^_`{\|}~]).*$", password):
            score +=1
    return score >= 3
