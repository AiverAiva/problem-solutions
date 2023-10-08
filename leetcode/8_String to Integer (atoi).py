class Solution(object):
    def myAtoi(self, s):
        regex, lim = re.findall(r'^(\s+)?([-+]?\d+)', s), 2**31
        return min(lim-1, max(-lim, int(regex[0][1]))) if regex else 0

        """
        :type s: str
        :rtype: int
        """
        