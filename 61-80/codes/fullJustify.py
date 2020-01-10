class Solution:
    def fullJustify(self, words, maxWidth):
        rel = []
        s = ''

        for i, a in enumerate(words):
            if len(s) + len(a) <= maxWidth:
                s += (a + ' ')
            else:
                s = s.rstrip()
                space_cnt = maxWidth - len(s)
                if space_cnt:
                    s = [temp + ' ' for temp in s.split(" ")]
                    s[-1] = s[-1].rstrip()
                    s_len = len(s)
                    if s_len == 1: s_len += 1
                    for j in range(space_cnt):
                        s[j % (s_len - 1)] += ' '
                rel.append("".join(s))
                s = a + " "
            if i == len(words) - 1:
                s = s.rstrip()
                s += (maxWidth - len(s)) * " "
                rel.append(s)
        return rel


    
def main():
    words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
    maxWidth = 16

    a = Solution()
    s = a.fullJustify(words, maxWidth)
    for i in s:
        print(i, len(i))


if __name__ == '__main__':
    main()
