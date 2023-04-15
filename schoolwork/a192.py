def cv(k, l):
    if len(l) == 1 and k > l[0]:
        print(k+l[0]) 
    elif k > l[0]:
        nl = list(l)
        nl.pop(0)
        cv(k+l[0], nl)
    else:
        print(k)

try:
    while(1):
        line1 = input()
        line2 = input()

        initial = int(line1.split(" ")[1])
        moblist =  list(map(lambda x: int(x), line2.split(" ")))
        cv(initial, moblist)

except EOFError as e:
   print(end="")

