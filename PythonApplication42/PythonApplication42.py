import sys
import re

stack = [None] * 16384
pc = 0

def parse(l,c = ' ',p = 0):
    loc = p
    l1 = l.strip().split(c)
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
            r = float(stack[loc-1]) + float(stack[loc-2])
            stack[loc-2] = r
            loc -= 1
        elif ll == 'SUB':
            r = float(stack[loc-1]) - float(stack[loc-2])
            stack[loc-2] = r
            loc -= 1
        elif ll == 'MUL':
            r = float(stack[loc-1]) * float(stack[loc-2])
            stack[loc-2] = r
            loc -= 1
        elif ll == 'DIV':
            r = float(stack[loc-1]) / float(stack[loc-2])
            stack[loc-2] = r
            loc -= 1
        elif ll == '<':
            stack[loc] = float(stack[loc-1]) < float(stack[loc-2])
            loc += 1
        elif ll == 'EXE':
            p = re.compile('{(.*)}')
            ll1 = p.match(stack[loc-1])
            parse(ll1.group(1),',',loc-1)
            loc -= 1
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
        else:
            pass
    return loc

fl = open(sys.argv[1],"r")
l = fl.readline()
#pc = parse(l)
#l = fl.readline()

while(l):
    pc = parse(l,' ',pc)
    l = fl.readline()

print(stack[0:30])



