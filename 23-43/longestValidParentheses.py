class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2: return 0

        def fingml(sta, n, step):
            left = right = 0
            temp = 0
            for i in range(sta, n, step):
                if s[i] == '(':
                    left += 1
                else:
                    right += 1
                if (right > left and step == 1) or (right < left and step == -1):
                    left = right = 0
                    continue
                if left == right and left + right > temp:
                    temp = left + right
            return temp

        return max(fingml(0, n, 1), fingml(n - 1, -1, -1))

def main():

    sw = [")()())", "()(())", ")((()((()()()())))(()()()()(())()"]
    a = Solution()
    for s in sw:
        print(a.longestValidParentheses(s))

if __name__ == '__main__':
    main()