class Solution:
    def minWindow(self, s: str, t: str):
        n = len(s)
        left = right = 0
        hs, ht = {i: 0 for i in t}, {}
        for i in t:
            ht[i] = ht.get(i, 0) + 1
        mlen = float('inf')
        ans = ""
        flag = False
        while right < n or flag:
            if not flag:
                if s[right] in t:
                    hs[s[right]] += 1
                right += 1
            else:
                while flag:
                    if right - left < mlen:
                        mlen = right - left
                        ans = s[left: right]
                    if s[left]in t:
                        hs[s[left]] -= 1
                        flag = True if hs[s[left]] >= ht[s[left]] else False
                    left += 1
            for i in hs:
                if hs[i] < ht[i]:
                    flag = False
                    break
                else:flag = True
        return ans
    
    
def main():
    s = "aa"
    t = "aa"
    a = Solution()
    print(a.minWindow(s, t))


if __name__ == '__main__':
    main()
