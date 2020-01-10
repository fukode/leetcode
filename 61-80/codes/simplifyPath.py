class Solution:
    def simplifyPath(self, p):

        def is_space(x):
            return True if x != '' else False
        p = list(filter(is_space, p.split('/')))

        res = []
        for i in p:
            if i == '..' and res:
                res.pop()
            elif i == '.' or i == '..':
                continue
            else:
                res.append(i)
        return "/" + "/".join(res)

    
def main():
    p = ""
    a = Solution()
    print(a.simplifyPath(p))


if __name__ == '__main__':
    main()
