class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        n = len(candidates)
        if not n or target < candidates[0]: return []
        rel = []

        def rb(candidates, target, re):
            if target < 0:
                return
            if target == 0 and re not in rel:
                rel.append(re)
            for i in range(len(candidates)):
                if candidates[i] > target:
                    break
                rb(candidates[i + 1:], target - candidates[i], re + [candidates[i]])
        rb(candidates, target, [])
        return rel

def main():
    candidates = [10,1,2,7,6,1,5]
    target = 8

    a = Solution()
    print(a.combinationSum2(candidates, target))

if __name__ == '__main__':
    main()