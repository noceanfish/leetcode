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
        total_zig = strLength // oneZig
        remain_element = strLength % oneZig
        columns = total_zig * (numRows - 2)
        if remain_element - numRows >= 0:
            columns = columns + 1 + (remain_element - numRows)
        else:
            columns = columns + 1

        index = 0
        zigM = [numRows * [''] for i in range(columns)]
        for i in range(total_zig):
            zigM[i * (numRows - 1)] = s[i * oneZig:i * oneZig + numRows]

            for j in range(numRows - 2):
                zigM[i * (numRows - 1) + j + 1][numRows - j - 1] = s[i * oneZig + numRows + j]

        res = ""
        for m in range(numRows):
            for n in range(columns):
                if zigM[n][m]: res = res + zigM[n][m]

        return res


def main():
    input = 'PAYPALISHIRING'
    n = 3
    slt = Solution()
    res = slt.convert(input, 3)
    print(res)


if __name__ == "__main__":
    main()
