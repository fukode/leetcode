"""
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""


class Solution:
    def isSameTree(self, p, q):
        s = []
        if (not q or not p) and p != q:
            return False
        while (p and q) or s:
            while p and q:
                s.append((p, q))
                p = p.left
                q = q.left
            if (not q or not p) and p != q:
                return False
            p, q = s.pop()
            if p.val != q.val:
                return False
            p = p.right
            q = q.right

        return True

    #         def bk(p, q):
    #             if not p and not q:
    #                 return True

    #             if p and q and p.val == q.val:
    #                 return bk(p.left, q.left) and bk(p.right, q.right)
    #             else:
    #                 return False

    #         return bk(p, q)
    
def main():
    p, q = None, None
    a = Solution()
    print(a.isSameTree(p, q))


if __name__ == '__main__':
    main()
