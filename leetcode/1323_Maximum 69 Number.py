#Runtime 6 ms Beats 95.74%
#Memory 13.3 MB Beats 33.58%

class Solution(object):
    def maximum69Number (self, num):
        digits=[i for i in str(num)]
        for i in range(len(digits)):
            if digits[i] == '6':
                digits[i]='9'
                break

        newNum = ""
        for i in digits:
            newNum += i
        return int(newNum)