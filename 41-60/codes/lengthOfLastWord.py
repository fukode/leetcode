class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastn = 0
        s = s.rstrip()
        for i in range(len(s) - 1, -1, -1):
            if not s[i].isspace():
                lastn += 1
            else:
                break
        return lastn
    
    
def main():
    s = "Hello World"
    a = Solution()
    print(a.lengthOfLastWord(s))


if __name__ == '__main__':
    main()
