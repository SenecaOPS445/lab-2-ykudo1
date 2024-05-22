#!/usr/bin/env python3

import sys
arguments = sys.argv[0]
#name = sys.argv[1]
#age = sys.argv[2]

#name = input("Name: ")
#age = input("Age: ")

if len(sys.argv) == 3:
    name = sys.argv[1]
    age = sys.argv[2]
    print('Hi ' + name + ', you are ' + age + ' years old.')


if len(sys.argv) != 3:
    print('Usage: ' + arguments + ' name' + ' age')
    sys.exit()

if len(sys.argv) == 0:
    print('Usage: ' + arguments + ' name' + ' age')
    sys.exit()

#if arguments != './lab2d.py':
#    print('Usage: ./lab2d.py name age')
#    sys.exit()


#if len(sys.argv) != 3:
#    print('Usage: ./lab2d.py name age')
#    sys.exit()


