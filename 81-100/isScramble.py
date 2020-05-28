class Solution:
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False

    
def main():
    # s1 = "great"
    # s2 = "rgtae"
    s1 = "abcde"
    s2 = "caebd"
    a = Solution()
    print(a.isScramble(s1, s2))


if __name__ == '__main__':
    main()
