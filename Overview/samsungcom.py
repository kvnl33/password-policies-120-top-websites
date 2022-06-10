#!/usr/bin/env python

#-----------------------------------------------------------------------
# samsungcom.py
# Author: Kevin Lee
#-----------------------------------------------------------------------

import re

#-----------------------------------------------------------------------

def samsung_passwordValidates(password):
    # "(Reverse-engineered: 3 of lowercase, uppercase, number, symbol) Using special characters, 
    # other than ~!@#$%^&*-_+=|"";[]{}()<>,./?\, is not allowed.
    # Use 8 or more characters with a mix of letters, numbers, and symbols.
    # Can't include more than 3 repeated or consecutive character in your password."
    # Space not allowed.
    score = 0
    if len(password) >= 8 and re.match(r"^(?!.*(.)\1\1\1).*$",password) and re.match(r"^(?!.*[\s]).*$", password):
        if re.match(r"^(?=.*[A-Z]).*$",password):
            score +=1
        if re.match(r"^(?=.*[a-z]).*$",password):
            score +=1
        if re.match(r"^(?=.*[\d]).*$",password):
            score +=1
        if re.match(r"^(?=.*[!\"#\$%&\'\(\)\*\+,\-\./:;<=>\?@\[\\\]\^_`{\|}~]).*$", password):
            score +=1
    return score >= 3
    