class Solution:
    def groupAnagrams(self, strs):

        # lookup = {}
        # for s in strs:
        #     if "".join(sorted(s)) not in lookup:
        #         lookup["".join(sorted(s))] = [s]
        #     else: lookup["".join(sorted(s))].append(s)
        # return list(lookup.values())
        x = 2
        n = 10
        def pw(x, n):
            if n == 1:
                return x
            x *= pw(x, n - 1)
            return x
        ans = pw(x, n)
        print(ans)

def main():
    s = ["eat", "tea", "tan", "ate", "nat", "bat"]
    a = Solution()
    print(a.groupAnagrams(s))

if __name__ == '__main__':
    main()