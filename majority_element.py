class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if str(num) in hashmap:
                hashmap[str(num)] +=1
            else:
                hashmap[str(num)] = 1
                
        maxfreq = 0
        maxkey = 0
        for key , value in hashmap.items():
            if value > maxfreq:
                maxfreq = value
                maxkey = int(key)

        return maxkey

