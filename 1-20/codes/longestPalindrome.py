import time

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # start = time.time()
        # size = len(s)
        # if size <= 1: return s

        # dp = [[False for _ in range(size)] for _ in range(size)]
        # rstr = s[0]
        # max_len = 1
        #
        # for r in range(1, size):
        #     for l in range(r):
        #         if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
        #             nowlen = r - l + 1
        #             dp[l][r] = True
        #             if nowlen > max_len:
        #                 max_len = nowlen
        #                 rstr = s[l : r + 1]
        # end = time.time()
        # print(end - start)

        size = len(s)
        if size <= 1: return s
        p = []
        ps = '#'
        rstr = s[0]
        for j in range(size):
            ps += s[j]
            ps += '#'

        id = mx = 0
        mxlen = 1
        ps_size = len(ps)
        for i in range(ps_size):
            if i < mx:
                p.append(min(p[2 * id - i], mx - i))
            else:
                p.append(1)

            while i - p[i] >= 0 and i + p[i] < ps_size and ps[i - p[i]] == ps[i + p[i]]:
                p[i] += 1

            if i + p[i] > mx:
                mx = i + p[i]
                id = i

            if p[i] - 1 > mxlen:
                mxlen = p[i] - 1
                rstr = ps[i - p[i] + 1: i + p[i]].replace('#', '')

        return rstr

def main():
    str = 'bb'
    #for i in range(1000):
      #  str = str + 'a'

    a = Solution()
    print(a.longestPalindrome(str))

if __name__ == '__main__':
    main()