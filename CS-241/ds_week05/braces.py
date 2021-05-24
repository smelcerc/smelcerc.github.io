file = input('File: ')
# /Users/smelcerc/Code/GitHub/smelcerc.github.io/CS-241/ds_week05/stacks06.txt
open_brace = []
close_brace = []
balanced = True
file = open(file, 'r')

while True:
    c = file.read(1)
    if not c:
        break
    
    if c == '(' or c == '{' or c == '[':
        open_brace.append(c)

    if c == ')' or c == '}' or c == ']':
        close_brace.append(c)
        if len(open_brace) == 0:
            balanced = False
            break
        popped = open_brace.pop()
        if (popped == '(' and c != ')') or (popped == '{' and c != '}') or (popped == '[' and c != ']'):
            balanced = False
            break
        if (popped == '(' and c == ')') or (popped == '{' and c == '}') or (popped == '[' and c == ']'):
            close_brace.pop()

file.close

if (len(open_brace) == 0) and (len(close_brace) == 0) and balanced == True:
    print('Balanced')
elif (len(open_brace) != 0) or (len(close_brace) != 0) or balanced == False:
    print('Not balanced')
