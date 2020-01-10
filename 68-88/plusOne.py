class Solution:
    def plusOne(self, digits):
        d = int(''.join(map(str, digits))) + 1
        return list(map(int, str(d)))
    
    
def main():
    digits = [4,3,2,1]
    a = Solution()
    print(a.plusOne(digits))


if __name__ == '__main__':
    main()
