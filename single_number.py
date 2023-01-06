class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
            
            # study more about bitwise operations AND OR NOT XOR
            
            
            
            
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            try:
                hashmap[num] +=1
            except:
                hashmap[num] = 1
    
        for key in hashmap:
            if hashmap[key] == 1:
                return key
        return 0
