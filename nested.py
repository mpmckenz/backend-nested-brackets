#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: Nested Bracket validator. Outputs bool and index of offending bracket
"""
__author__ = "Michael_McKenzie"

import sys

closers = [")", "]", "}", ">", "*)"]
openers = ["(", "[", "{", "<", "(*"]


def is_nested(line):
    stack = []
    counter = 0
    while line:
        counter += 1
        token = line[0]
        if line.startswith("(*") or line.startswith("*)"):
            token = line[:2]
        if token in openers:
            stack.append(token)
        elif token in closers and openers[closers.index(token)] != stack.pop():
            return "No " + str(counter)
        line = line[len(token):]
    if stack:
        return "No " + str(counter)
    else:
        return "Yes"


def main(args):
    # if len(sys.argv) != 2:
    #     sys.exit(1)
    with open("input.txt") as f:
        with open('output.txt', 'w') as o:
            for expression in f.readlines():
                result = is_nested(expression)
                print result
                o.write(result + '\n')


if __name__ == '__main__':
    main(sys.argv)
