class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if (not s and len(s) == 1): return s

        length = len(s)
        result = ""
        maxlength = 0
        for i in range(length):
            maxlength = len(result)
            # single center
            res = self.checker(s, i, i)
            if len(res) >= maxlength:
                result = res
                maxlength = len(result)

            # double center
            res2 = self.checker(s, i, i + 1)
            if len(res2) >= maxlength:
                result = res2
                maxlength = len(result)

        return result

    def checker(self, s, start, end):

        length = len(s)
        while start >= 0 and end < length and s[start] == s[end]:
            start = start - 1
            end = end + 1

        return s[start+1:end]


def main():
    s = 'babad'
    sl = Solution()
    res = sl.longestPalindrome(s)
    print(res)


if __name__ == "__main__":
    main()
