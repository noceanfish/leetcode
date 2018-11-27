class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s or not p: return False

        s_index = 0
        p_index = 0
        sLen = len(s)
        pLen = len(p)

        while s_index < sLen:
            if p_index >= pLen: return False

            if s[s_index] == p[p_index] or p[p_index] == '.':
                s_index += 1
                p_index += 1
            elif p[p_index] == '*':
                if p_index == 0:
                    return False
                if s[s_index] == p[p_index - 1]:
                    s_index += 1
                elif p[p_index - 1] == '.':
                    s_index += 1
                elif p_index + 1 < pLen and s[s_index] == p[p_index + 1]:
                    s_index += 1
                    p_index += 2
                elif p_index + 1 < pLen and p[p_index + 1] == '.':
                    s_index += 1
                    p_index += 2
                else:
                    return False
            elif p_index + 1 < pLen and p[p_index + 1] == '*':
                p_index += 2
            else:
                return False

        return True


def main():
    s = "mississippi"
    p = "mis*is*ip*."

    slt = Solution()
    res = slt.isMatch(s, p)
    print(res)


if __name__ == "__main__":
    main()