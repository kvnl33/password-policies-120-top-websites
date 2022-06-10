This repository contains the dataset from our SOUPS 2022 paper *Password policies of most top websites fail to follow best practices*.

Our project website can be found [here](https://passwordpolicies.cs.princeton.edu/).

### Overview

- ```overview.xlsx``` contains our full findings, including raw text we extracted, regular expressions, and websites we had skipped.
- Some of the regular expressions that could not be easily-encoded are in ```*.py``` files.

### Study 1 - Password Blocking

- ```*.tsv``` files contain the passwords we tested at each website. Each line also contains the password's guess number, as determined by [PGS](https://pgs.ece.cmu.edu/). 

### Study 2 - Strength Meters

- ```psm-findings.xlsx``` contains our findings on password strength meters.

