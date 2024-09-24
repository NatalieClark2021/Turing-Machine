
tuples = []
print("Enter 5-Tuples. A . by itself to end.")

while True:
    line = input()
    i = 0
    s, r, w, m , c = ' ',' ',' ',' ',' '
    #state, read, write, direction, movestate
    if line == ".":
        break
   
    for ch in line:
        if i == 0:
            s = ch
        elif i==1:
            r = ch
        elif i == 2:
            w = ch
        elif i == 3:
            m = ch
        elif i == 4:
            c = ch
        
        i += 1
    tup = (s,r,w,m,c)
    tuples.append(tup)

state = tuples[0][0]

tapeInput = list(input("Enter initial tape: \n"))
    
it   = int(input("Iterations: "))
i = 0
tapePoint = 0

while i <= it:
    print(''.join(tapeInput[:tapePoint]) + "{"+state +"}"+  ''.join(tapeInput[tapePoint:]))

    if i == it:
        print("Iterations complete\n" + "Final State: " + state)
        break
    
    if tapePoint < len(tapeInput):
        tapeCh = tapeInput[tapePoint]
    else:
        tapeCh = ' '
    
    found = False
   
    for tup in tuples:
        
        if (tup[0] == state and tup[1] == tapeCh):
            
            w, m, c = tup[2], tup[3],tup[4]
            if len(tapeInput) <= tapePoint:
                tapeInput.append(' ') 
            tapeInput[tapePoint] = w 
        
            if m == 'R':
                tapePoint +=1
            elif m == 'L':
                if tapePoint > 0: 
                    tapePoint -= 1
                elif tapePoint == 0:
                  tapeInput.insert(0, ' ')
                  tapePoint = 0

            elif m == 'N':
                tapePoint = tapePoint 

            state = c   
            found = True
            break
        
    if(found == False):
        print("HALT(no transition found)\n" + "Final State: " + state) 
        break
    
    i +=1
    

        