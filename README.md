This repository contains the dataset from our SOUPS 2022 paper *Password policies of most top websites fail to follow best practices*. We visited websites from October 2021 to December 2021.

Our project website can be found [here](https://passwordpolicies.cs.princeton.edu/).

### Overview

- ```overview.xlsx``` contains our full findings, including raw text we extracted, regular expressions, and websites we had skipped.
- Some of the regular expressions that could not be easily-encoded are in ```*.py``` files.

### Study 1 - Password Blocking

- ```*.tsv``` files contain the passwords we tested at each website. Each line contains the password's guess number as determined by [PGS](https://pgs.ece.cmu.edu/), and whether or not it was accepted by the website. For tested *leaked* passwords, we also include the position of the passwords on the [HIBP-NCSC-100k list](https://www.ncsc.gov.uk/blog-post/passwords-passwords-everywhere). 

### Study 2 - Strength Meters

- ```psm-findings.xlsx``` contains our findings on password strength meters.
- ```*.tsv``` files contain the 100 *easiest-guessed* passwords tested at each website's strength meter. Each line contains the password's guess number as determined by [PGS](https://pgs.ece.cmu.edu/), and its feedback on the strength meter (1 being the lowest, refer to ```psm-findings.xlsx``` for scale).

