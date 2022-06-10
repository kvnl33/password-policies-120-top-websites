#!/usr/bin/env python

#-----------------------------------------------------------------------
# huffingtonpostcom.py
# Author: Kevin Lee
#-----------------------------------------------------------------------

import re

#-----------------------------------------------------------------------

def huffingtonpost_passwordValidates(password):
    #   At least 8 characters in length   Contain at least 3 of the following 4 types of characters:   
    #   Lower case letters (a-z)   Upper case letters (A-Z)   Numbers (i.e. 0-9)   
    #   Special characters (e.g. !@#$%^&*)
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
