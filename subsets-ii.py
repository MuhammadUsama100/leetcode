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
        # to create a unique list of list in python use itertools.groupby eg : [[1,2,3] , [3,3,1,5],[3,3,1,5]] = [[1,2,3] , [3,3,1,5]]
        s.sort()
        return list(s for s, _ in itertools.groupby(s))
