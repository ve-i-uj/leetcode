"""38. Count and Say

https://leetcode.com/problems/count-and-say/
"""


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.countAndSay(*args, **kwargs)

    def countAndSay(self, n: int) -> str:
        res: str = '1'
        for _ in range(n - 1):
            cntr = [[res[0], 1]]
            for ch in res[1:]:
                last: str = cntr[-1][0]
                if last == ch:
                    cntr[-1][1] += 1
                    continue
                cntr.append([ch, 1])
                last = ch
            res = ''.join(f'{cnt}{ch}' for ch, cnt in cntr)

        return res