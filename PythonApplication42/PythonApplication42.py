import sys
import re

MEMSIZE = 16*1024*1024
op = {'STO':1, 'ADD':2, 'SUB':3, 'MUL':4, 'DIV':5, 'JMP': 6}

loc = 0

stack = [0.0] * MEMSIZE

#def enc(m1: int, m2: int, op: str, typ: int):
#    res = 0
#    if typ == 1:
#        # memory-to-memory operation
#        if op == "STO":
#            res += m1 << 35
#            res += m2 << 7
#            res += typ << 3
#            res += 1
#    elif typ == 2:
#        # storing an actual number
#        if op == "STO":
#            res += m1 << 35
#            res += m2 << 3  
#            res += typ << 3
#            res += 1
#    if res < 0 :
#        res = res & 0xffffffffffffffff
#    return res

#def dec(mem: int, typ: int):
#    if typ == 1:
#        d1 = mem >> 35 & 0xfffffff
#        d2 = mem >> 7 & 0xfffffff
#        d3 = mem >> 3 & 0xf
#        d4 = mem & 0xf
#        return [d1,d2,d3,d4]
#    elif typ == 2:
#        d1 = mem >> 35 & 0xfffffff
#        d2 = mem >> 3 & 0xfffffffff
#        d4 = mem & 0xf
#        return [d1,d2,d4]
    
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
    l = fl.readline()

print(stack[0:10])



