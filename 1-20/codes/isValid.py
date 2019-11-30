class Solution:
    def isValid(self, s: str) -> bool:
        va = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        ss = []
        for i in s:
            if i not in va:
                ss.append(i)
            else:
                if ss == []:
                    return False
                if ss.pop() != va[i]:
                    return False

        return not ss

def main():

    s = "}"
    a = Solution()
    print(a.isValid(s))

if __name__ == '__main__':
    main()