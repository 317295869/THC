#!/usr/bin/python3.7
#
# Eduardo Alexis Valencia Dorantes
# Python 3.7.3
#
#
#

newlist = []
n = input()

arr = input()
arr = arr.split()
arr = list(map(int,arr))

winner = arr[0]

for n in arr:
    if n > winner:
        winner = n

for i in arr:
    if i < winner:
        newlist.append(i)

runnerup = newlist[0]

for k in newlist:
    if k > runnerup:
        runnerup = k


print(runnerup)
