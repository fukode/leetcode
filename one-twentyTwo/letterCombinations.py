class Solution:
    def letterCombinations(self, digits: str):
        letter = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        i, n = 0, len(digits)
        if n < 1: return []

        def p(i):
            if i < n - 1:
                res = []
                temp = p(i + 1)
                for k in letter[int(digits[i])]:
                    res.append([(k + j) for j in temp])
                return sum(res, [])
            else: return [j for j in letter[int(digits[i])]]

        return p(i)

def main():

    a = Solution()
    print(a.letterCombinations("234"))

if __name__ == '__main__':
    main()