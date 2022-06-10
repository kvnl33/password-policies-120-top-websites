#!/usr/bin/env python

#-----------------------------------------------------------------------
# githubcom.py
# Author: Kevin Lee
#-----------------------------------------------------------------------

import re

#-----------------------------------------------------------------------

def github_passwordValidates(password):
    # Make sure it's at least 15 characters OR at least 8 characters including a number and a lowercase letter.
    if len(password) >= 15:
        return True
    elif re.match(r"^(?=.*[a-z])(?=.*\d).{8,}$",password):
        return True
    else:
        return False
        