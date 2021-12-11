import sys
import re

stack = []
ltmp1 = []
pc = 0

def parse(l,c = ' ',p = 0):
    global stack
    l1 = l.strip().split(c)
    r = 0.0
    for ll in l1:
        if  ll.isdecimal():
            stack.append(float(ll))
        elif ll == 'DUP':
            stack.append(stack[-1])
        elif ll == 'POP':
            stack.pop()
        elif ll == 'ADD':
            stack.append(float(stack.pop()) + float(stack.pop()))
        elif ll == 'SUB':
            stack.append(-float(stack.pop()) + float(stack.pop()))
        elif ll == 'MUL':
            stack.append(float(stack.pop()) * float(stack.pop()))
        elif ll == 'DIV':
            stack.append(1.0/float(stack.pop()) * float(stack.pop()))
        elif ll == '<':
            stack.append(float(stack.pop()) < float(stack.pop()))
        elif ll == '=':
            stack.append(float(stack.pop()) == float(stack.pop()))
        elif ll == 'RE1':
            pass
        elif ll == 'EXE':
            p = re.compile('{(.*)}')
            ll1 = p.match(stack.pop())
            parse(ll1.group(1),',')
        elif ll == '.':
            print(stack[-1])
        elif list(ll)[0] == '[':
            p = re.compile('\[(\d+),(\d+)\]')
            ll1 = p.match(ll)
            stack.append(ll1.group(1) if stack[-1] else ll1.group(2))
        elif list(ll)[0] == '{':
            stack.append(ll)
        else:
            pass

fl = open(sys.argv[1],"r")
l = fl.readline()
#pc = parse(l)
#l = fl.readline()

while(l):
    parse(l,' ')
    l = fl.readline()

print(stack[0:30])



