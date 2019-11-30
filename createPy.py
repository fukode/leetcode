import os

def main():
    s = input("name: ")
    pm = input("paraments:").split(' ')
    fp = open(s+".py", 'w')
    pms = ', '.join([i for i in pm])
    ss = \
f"""class Solution:
    def {s}(self, {pms}):
    
    
def main():
    {pms} = 
    a = Solution()
    print(a.{s}({pms}))


if __name__ == '__main__':
    main()
"""
    fp.write(ss)
    fp.close()


if __name__ == '__main__':
    main()
