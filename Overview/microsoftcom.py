#!/usr/bin/env python

#-----------------------------------------------------------------------
# microsoftcom.py
# Author: Kevin Lee
#-----------------------------------------------------------------------

import re

#-----------------------------------------------------------------------

def microsoft_passwordValidates(password):
    # Passwords must have at least 8 characters and contain at least two of the following: 
    # uppercase letters, lowercase letters, numbers, and symbols.
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
    return score >= 2
    