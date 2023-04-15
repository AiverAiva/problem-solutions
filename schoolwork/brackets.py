def b(n):
    res = []
    def backtrack(s, left, right):
        if left == 0 and right == 0:
            res.append(s)
            return
        if left > 0:
            backtrack(s+'(', left-1, right)
        if right > left:
            backtrack(s+')', left, right-1)
    backtrack("", n, n)
    return res

try:
    while(1):
        for i in b(int(input())):
            print(i)
except EOFError as e:
   print(end="")

