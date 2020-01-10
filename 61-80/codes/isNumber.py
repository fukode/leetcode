class Solution:
    def isNumber(self, s):
        s = s.strip()
        dot_seen = False
        e_seen = False
        num_seen = False

        for i, a in enumerate(s):
            if a.isdigit():
                num_seen = True
            elif a == '.':
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            elif a == 'e':
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_seen = False
            elif a in "-+":
                if i > 0 and s[i - 1] != 'e':
                    return False
            else:
                return False

        return num_seen
def main():
    s = "53.5e93"
    a = Solution()
    print(a.isNumber(s))


if __name__ == '__main__':
    main()
