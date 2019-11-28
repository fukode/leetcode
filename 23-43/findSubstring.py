class Solution:
    # def findSubstring(self, s: str, words):
        # if not words or not s:return []
        # n, m = len(s), len(words[0])
        # w = words.copy()
        # if len("".join(w)) > n: return []
        # res = []
        # for i in range(n - m + 1):
        #     w = words.copy()
        #     if s[i:i+m] in w:
        #         j = i + m
        #         w.remove(s[i:i+m])
        #         while w:
        #             if s[j:j + m] in w:
        #                 w.remove(s[j:j+m])
        #                 j += m
        #             else:
        #                 break
        #         else:
        #             res.append(i)
        #             i = j
        #
        # return res

    def findSubstring(self, s: str, words):
        from collections import Counter
        if not s or not words: return []
        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, n - all_len + 1):
            tmp = s[i:i + all_len]
            c_tmp = []
            for j in range(0, all_len, one_word):
                c_tmp.append(tmp[j:j + one_word])
            if Counter(c_tmp) == words:
                res.append(i)
        return res


def main():
    s ="aaaaaaaa"
    words =["aa", "aa", "aa"]
    a = Solution()
    print(a.findSubstring(s, words))

if __name__ == '__main__':
    main()