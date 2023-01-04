class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size =  len(nums)
        found = 0
        i =0
        while i <=size -1:
            if nums[i] == val:
                found+=1
                for j in range(i+1 , size):
                    nums[j-1] = nums[j]
                nums[-1] = "_"
               
                i=-1
            i+=1

        return size - found

# Note python Loops work quite diffrent then the other programming language.
