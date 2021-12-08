import sys
import re

loc = 0

stack = []

fl = open(sys.argv[1],"r")
l = fl.readline()
lib = False

while(l):
    l1 = l.strip().split(' ')
    r = 0.0
    for ll in l1:
        if  ll.isdecimal():
            stack[loc] = float(ll)
            loc += 1
        elif ll == 'DUP':
            stack[loc] = stack[loc-1]
            loc += 1
        elif ll == 'POP':
            loc -= 1
        elif ll == 'ADD':
            r = stack[loc-1] + stack[loc-2]
            stack[loc-2] = r
            loc -= 1
        elif ll == 'SUB':
            r = stack[loc-1] - stack[loc-2]
            stack[loc-2] = r
            loc -= 1
        elif ll == 'MUL':
            r = stack[loc-1] * stack[loc-2]
            stack[loc-2] = r
            loc -= 1
        elif ll == 'DIV':
            r = stack[loc-1] / stack[loc-2]
            stack[loc-2] = r
            loc -= 1
        elif ll == '<':
            stack[loc] = stack[loc-1] < stack[loc-2]
            loc += 1
        elif ll == '.':
            print(stack[loc-1])
        elif list(ll)[0] == '[':
            p = re.compile('\[(\d+),(\d+)\]')
            ll1 = p.match(ll)
            stack[loc] = ll1.group(1) if stack[loc-1] else ll1.group(2)
            loc += 1
        elif list(ll)[0] == '{':
            stack[loc] = ll
            loc += 1
    l = fl.readline()

print(stack[0:10])



