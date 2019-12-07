class Solution:
    def generateParenthesis(self, n: int):
        # rel = []
        #
        # def bt(s='', left=0, right=0):
        #     if len(s) == 2 * n:
        #         rel.append(s)
        #     if left < n:
        #         bt(s + '(', left + 1, right)
        #     if right < left:
        #         bt(s + ')', left, right + 1)
        # bt()
        #
        # return rel
        if n == 0:
            return []
        total_l = []
        total_l.append([None])
        total_l.append(["()"])
        for i in range(2, n + 1):  # 开始计算i时的括号组合，记为l
            l = []
            for j in range(i):  # 遍历所有可能的括号内外组合
                now_list1 = total_l[j]
                now_list2 = total_l[i - 1 - j]
                for k1 in now_list1:  # 开始具体取内外组合的实例
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = k2 + "(" + k1 + ")"
                        l.append(el)
            total_l.append(l)
        return total_l[n]


def main():
    a = Solution()
    print(a.generateParenthesis(4))


if __name__ == '__main__':
    main()