class Solution:
    def insert(self, intervals, newInterval):
        n = len(intervals)
        if not n: return [newInterval]
        if newInterval[1] < intervals[0][0]: return [newInterval] + intervals
        if newInterval[0] > intervals[-1][-1]: return intervals + [newInterval]
        # for i in range(n):
        #     if newInterval[0] <= intervals[i][1]:
        #         left = i if intervals[i][1] >= newInterval[0] else i + 1
        #         for j in range(i, n):
        #             if newInterval[1] <= intervals[j][0] or j == n - 1:
        #                 right = j if newInterval[1] >= intervals[j][0] else j - 1
        #                 newInterval = [min(intervals[left][0], newInterval[0]), max(intervals[right][1], newInterval[1])]
        #                 return intervals[:left] + [newInterval] + intervals[right + 1:]
        #
        #     if i == n - 1:
        #         right = n - 1 if newInterval[0] <= intervals[-1][-1] else n
        #         if right == n - 1:
        #             newInterval = [min(intervals[right][0], newInterval[0]), max(intervals[right][1], newInterval[1])]
        #         return intervals[:right] + [newInterval]
        i = 0
        while i < n and newInterval[0] > intervals[i][1]: i += 1
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            intervals.pop(i)
            n -= 1
        intervals.insert(i, newInterval)
        return intervals


def main():
    intervals = [[1,5]]
    newInterval = [2,3]
    a = Solution()
    nums = a.insert(intervals, newInterval)
    print(nums)

if __name__ == '__main__':
    main()
