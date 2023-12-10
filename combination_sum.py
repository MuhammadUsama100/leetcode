class Solution(object):
    def combinationSum(self, candidates, target):
        def backtrack(start , target , path):
            if target == 0:
                result.append(list(path))
                return 
            for i in range(start , len(candidates)):
                if target - candidates[i] >= 0:
                    path.append(candidates[i])
                    backtrack(i,target-candidates[i],path)
                    path.pop()
        result = []
        candidates.sort()
        backtrack(0,target,[])
        return result
