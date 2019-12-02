#!/usr/bin/python3.7
#
# Valencia Dorantes Eduardo Alexis
# Python 3.7.3
#
#


def is_leap(year):
    leap = False
    
    if year%400==0:
        leap=True
    elif year%4==0 and year%100!=0:
        leap=True

    return leap
