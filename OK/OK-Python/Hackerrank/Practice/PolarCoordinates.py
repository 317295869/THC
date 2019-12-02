#!/usr/bin/python3.7
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
#
#
#

import cmath

n = input()

print(*cmath.polar(complex(n)), sep='\n')

