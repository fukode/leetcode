class Solution:
    def combinationSum(self, candidates, target: int):
        candidates.sort()
        re = []
        i, n = 0, len(candidates)

        def rb(s, snum, index):
            if (target - s) // candidates[index] < 1: return
            temp = (target - s) // candidates[index]
            snum.extend([candidates[index]] * temp)
            if (target - s) % candidates[index] == 0 and snum not in re:
                re.append(snum.copy())
                temp -= 1
                snum.pop()
            s += temp * candidates[index]
            while temp:
                for j in range(index + 1, n):
                    if (s + candidates[j]) <= target:
                        rb(s, snum, j)
                    else: break
                s -= candidates[index]
                snum.pop()
                temp -= 1

        while i < n:
            if candidates[i] > target:break
            rb(0, [], i)
            i += 1
        return re

def main():
    candidates = [2, 3, 5]
    target = 14

    a = Solution()
    print(a.combinationSum(candidates, target))

if __name__ == '__main__':
    main()