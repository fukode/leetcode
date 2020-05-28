class Solution:
    def restoreIpAddresses(self, s):
        res = []

        def bk(s, ip):
            if len(s) == 0 and ip.count('.') == 3:
                res.append(ip)
                return
            if ip.count('.') == 3 and int(s[:]) > 255:
                return

            if ip.count('.') == 3:
                if len(s) == 1 or s[0] != '0':
                    bk("", ip + s[:])
            else:
                for i in range(1, min(len(s), 4)):
                    if int(s[:i]) > 255 or (i > 1 and s[0] == '0'):continue
                    bk(s[i:], ip + s[:i] + '.')
        bk(s, "")
        return res


def main():
    s = "172162541"
    a = Solution()
    print(a.restoreIpAddresses(s))


if __name__ == '__main__':
    main()
