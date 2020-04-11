class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def helper(strs, cur_idx, ip_list):
            if len(strs) > 3 * (4 - cur_idx):
                return
            if cur_idx == 4 and not strs:
                res.append('.'.join(ip_list))
            if not strs:
                return
            if strs[0] == '0':
                ip_list.append(strs[0])
                helper(strs[1:], cur_idx + 1, ip_list)
                ip_list.pop()
            else:
                for i in range(1, min(3, len(strs)) + 1):
                    if -1 < int(strs[:i]) < 256:
                        ip_list.append(strs[:i])
                        helper(strs[i:], cur_idx + 1, ip_list)
                        ip_list.pop()

        helper(s, 0, [])
        return res
