class Solution(object):
    def removeElement(self, nums, val):
      rem_index = -1
      index = 0
      while index < len(nums):
        if (nums[index] == val):
          nums[index] = nums[rem_index]
          nums[rem_index] = -1000
          rem_index -=1
          continue
        index+=1
      return len(nums)+1 - (rem_index *-1)


# with this question you will learn about the constraints and manipulating the arrays
