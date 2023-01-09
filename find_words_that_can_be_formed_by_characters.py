import copy

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashmap ={}
        for c in chars:
            try:
                hashmap[c] += 1
            except:
                hashmap[c] = 1
        totalLength = 0
        f =  False
        for word in words:
            hashmap2 = copy.deepcopy(hashmap)
            f =  False
            for c in word:
                if c in hashmap2 and hashmap2[c] > 0:
                    hashmap2[c] -=1
                    f =  True
                else :
                    f =  False
                    break
            if f :
                totalLength+= len(word)
        return totalLength


                

