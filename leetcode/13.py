class Solution(object):
    def romanToInt(self, s):
        uwu = []
        c = 0
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        li = list(s)
        owo = list(map(lambda x: dict[x], li))
        while len(owo)>0:
            try:
                if owo[0] < owo[1]:
                    uwu.append(owo[1] - owo[0])
                    owo.pop(0)
                    owo.pop(0)
                else:
                    uwu.append(owo[0])
                    owo.pop(0)
            except:
                uwu.append(owo[0])
                owo.pop(0)
                
        for i in uwu:
            c+=i
        return c