#!/usr/bin/env python

#-----------------------------------------------------------------------
# chasecom.py
# Author: Kevin Lee
#-----------------------------------------------------------------------

import re

#-----------------------------------------------------------------------

def chase_passwordValidates(password):
    # Please tell us a new password. It must be between 8-32 characters and 
    # include at least 2 of the following elements: 1 letter (case sensitive), 
    # 1 number and at least 1 of the following special characters: ! # $ % + / = @ ~.
    # 
    # Anything not in symbol space is not allowed
    score = 0
    if len(password) >= 8 and len(password) <= 32 and re.match(r"^(?!.*(.)\1\1)(?!.*[\s\"&\'\(\)\*,\-\.:;<>\?\[\\\]\^_`{\|}]).*$", password):
        if re.match(r"^(?=.*[A-Za-z]).*$",password):
            score +=1
        if re.match(r"^(?=.*[\d]).*$",password):
            score +=1
        if re.match(r"^(?=.*[!#\$%\+/=@~]).*$", password):
            score +=1
    return score >= 2
