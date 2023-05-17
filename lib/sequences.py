#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = [0,1]
    i, j = 0, 1 

    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        while len(fib_list) < length:
            fib_list.append(fib_list[i] + fib_list[j])
            i += 1
            j += 1        
        print(fib_list)



# print(print_fibonacci(10))