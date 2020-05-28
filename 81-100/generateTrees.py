# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int):

        def generate(start, end):
            if start > end:
                return [None,]
            res = []

            for i in range(start, end + 1):
                left = generate(start, i - 1)
                right = generate(i + 1, end)

                for l in left:
                    for r in right:
                        current = TreeNode(i)
                        current.left = l
                        current.right = r
                        res.append(current)
            return res
        return len(generate(1, n)) if n else 0


def main():
    for i in range(1, 8):
        a = Solution()
        print(a.generateTrees(i))


if __name__ == '__main__':
    main()
