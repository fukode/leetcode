class Solution:
    def grayCode(self, n):
        # nums = [0]
        # n = 2 ** n
        # temp = ['0'] * n
        # i = 1
        # while i < n:
        #     temp[-1] = '0' if temp[-1] == '1' else '1'
        #     nums.append(int("".join(temp), 2))
        #     i += 1
        #     if i == n: break
        #
        #     for j in range(len(temp) - 1, -1, -1):
        #         if temp[j] == '1':
        #             temp[j - 1] = '0' if temp[j - 1] == '1' else '1'
        #             nums.append(int("".join(temp), 2))
        #             i += 1
        #             break
        #
        # return nums

        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res


    
def main():
    n = 5
    a = Solution()
    print(a.grayCode(n))
# [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8,24,25,27,26,30,31,29,28,20,21,23,22,18,19,17,16]

if __name__ == '__main__':
    main()
