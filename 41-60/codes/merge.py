class Solution:
    def merge(self, intervals):
        n = len(intervals)
        intervals.sort()
        print(intervals)
        i = 1
        while i < n:
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1] = [intervals[i - 1][0], max(intervals[i][1], intervals[i - 1][1])]
                intervals.pop(i)
                n -= 1
            else:
                i += 1

        return intervals

def main():
    s = [[2,4],[2,3],[6,7],[8,9],[1,10]]
    a = Solution()
    nums = a.merge(s)
    print(nums)

if __name__ == '__main__':
    main()