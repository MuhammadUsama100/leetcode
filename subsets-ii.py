import itertools


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s = [[]]
        for i in range(1, len(nums)+1):
            combs = itertools.combinations(nums, i)
            for c in list(combs):
                c = list(c)
                c.sort()
                s.append(c)

        s.sort()
        return list(s for s, _ in itertools.groupby(s))
