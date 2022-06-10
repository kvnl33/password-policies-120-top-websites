#!/usr/bin/env python

#-----------------------------------------------------------------------
# digicertcom.py
# Author: Kevin Lee
#-----------------------------------------------------------------------

import re

#-----------------------------------------------------------------------

def digicert_passwordValidates(password):
    # Your password must be at least 10 characters long and contain 3 of the following:
    # lowercase letter, capital letter, number, or symbol
    # Space doesn't count. " doesn't count. ' doesn't count. \ doesn't count. _ doesn't count. ` doesn't count. | doesn't count. 
    score = 0
    if len(password) >= 10:
        if re.match(r"^(?=.*[A-Z]).*$",password):
            score +=1
        if re.match(r"^(?=.*[a-z]).*$",password):
            score +=1
        if re.match(r"^(?=.*[\d]).*$",password):
            score +=1
        if re.match(r"^(?=.*[!#\$%&\(\)\*\+,\-\./:;<=>\?@\[\]\^{}~]).*$", password):
            score +=1
    return score >= 3
    