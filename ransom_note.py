class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hashmap = {}
        for m in magazine:
            try:
                hashmap[m] +=1
            except:
                hashmap[m] = 1   # use try catch to check if the key exist in python on O(1) time complexity

        for val in ransomNote:
            if val in hashmap and hashmap[val] > 0 :
                hashmap[val] -=1
            else :
                return False
        return True
