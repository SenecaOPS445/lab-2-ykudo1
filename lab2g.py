#!/usr/bin/env python3
#Author:Yuna Kudo
#Author ID:187227210
#Date Created:20240522

import sys

if len(sys.argv) == 1:
    timer = 3
    while timer != 0:
        print(timer)
        timer = timer - 1
    print('blast off!')

else:
    timer = int(sys.argv[1])
    while timer != 0:
        print(timer)
        timer = timer - 1
    print('blast off!')
