#!/usr/bin/env python

#-----------------------------------------------------------------------
# amazonawscom.py
# Author: Kevin Lee
#-----------------------------------------------------------------------

import re

#-----------------------------------------------------------------------

def aws_passwordValidates(password):
    # Your password must: be a minimum of 8 or more characters include a minimum of three of the following 
    # mix of character types: uppercase, lowercase, numbers, non-alphanumeric symbols, 
    # for example !@#$%^&*()_+-=[]{}|' not be identical to your AWS account name or email address
    # Space doesnt count. " doesnt count. , doesnt count. . doesnt count. / doesnt count. : doesnt count. 
    # ; doesnt count. < doesnt count. > doesnt count. ? doesnt count. \ doesnt count ` doesnt count
    score = 0
    if len(password) >= 8:
        if re.match(r"^(?=.*[A-Z]).*$",password):
            score +=1
        if re.match(r"^(?=.*[a-z]).*$",password):
            score +=1
        if re.match(r"^(?=.*[\d]).*$",password):
            score +=1
        if re.match(r"^(?=.*[!#\$%&\'\(\)\*\+\-=@\[\]\^_{\|}~]).*$", password):
            score +=1
    return score >= 3
    