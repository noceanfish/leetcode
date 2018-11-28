class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str_noSpace = str.strip()
        if not str_noSpace: return 0
        # if str_noSpace[0] not in '+-[0-9]'： return 0
        if str_noSpace[0] not in "+-0123456789": return 0

        initial = str_noSpace[0]
        positive = True
        if initial == "-":
            positive = False
            clean_str = str_noSpace[1:]
        elif initial == "+":
            clean_str = str_noSpace[1:]
        else:
            clean_str = str_noSpace[0:]

        index = 0
        res = 0
        length = len(clean_str)
        # while (index < length and clean_str[index] in '0123456789' ):
        while (index < length and clean_str[index].isdigit()):
            if index == 0:
                res = int(clean_str[index])
            else:
                res = int(clean_str[index]) + res * 10
            index += 1

        if positive:
            return res if res < 2 ** 31 - 1 else 2 ** 31 - 1
        else:
            return -res if -res > -2 ** 31 else -2 ** 31

    def main(self):
        str = "  -42"
        res = self.myAtoi(str)
        print(res)


if __name__ == "__main__":
    Solution().main()
