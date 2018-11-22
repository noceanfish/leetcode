class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s: return s
        if numRows <= 1: return s

        # format the string into matrix base on numRows*colimns
        strLength = len(s)
        oneZig = numRows + numRows - 2
        total_zig = strlength // oneZig
        remain_element = strlength % oneZig
        columns = total_zig * (numRows - 2)
        if remain_element - numRows >= 0:
            columns = columns + 1 + (remain_element - numRows)
        else:
            columns = columns + 1

        index = 0
        zigM[numRows][columns] = []
        for i in range(total_zig):
            zigM[i * (numRows - 1)] = s[i * oneZig:i * oneZig + numRows]

        while (index < strlength):


def main():
    slt = Solution()
    res = slt.convert()
    print(res)


if __name__ == "__main__":
    main()
