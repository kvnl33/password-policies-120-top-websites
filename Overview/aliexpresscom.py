#!/usr/bin/env python

#-----------------------------------------------------------------------
# aliexpresscom.py
# Author: Kevin Lee
#-----------------------------------------------------------------------

import re

#-----------------------------------------------------------------------

def aliexpress_passwordValidates(password):
    # Uppercase letters, lowercase letters, numbers and punctuation includes at least 2 
    # Can contain only letters, numbers and punctuation marks (except spaces) 6-20 characters
    # " not allowed. ' not allowed. \ not allowed. Space not allowed
    score = 0
    if len(password) >= 6 and len(password) <= 20 and re.match(r"^(?!.*[\s\'\"\\]).*$", password):
        if re.match(r"^(?=.*[A-Z]).*$",password):
            score +=1
        if re.match(r"^(?=.*[a-z]).*$",password):
            score +=1
        if re.match(r"^(?=.*[\d]).*$",password):
            score +=1
        if re.match(r"^(?=.*[!#\$%&\(\)\*\+,\-\./:;<=>\?@\[\]\^_`{\|}~]).*$", password):
            score +=1
    return score >= 2
