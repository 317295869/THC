#!/usr/bin/python3.7
#
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
#
#
#


dictionary = {}

n = int(input())

for i in range(n):
    string = input().split()
    name = string[0]
    math = float(string[1])
    physics = float(string[2])
    chemistry = float(string[3])
    grades = [math,physics,chemistry]
    dictionary[name] = [grades]

student = input()

def avg(student):
    studentmath = dictionary[student][0]
    studentphysics = dictionary[student][1]
    studentchemistry = dictionary[student][2]
    average = (studentmath + studentphysics + studentchemistry)/3
    return(average)

print(avg(student))
