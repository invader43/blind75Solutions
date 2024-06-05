class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1

        sum = None 
        #2 pointers 
        while not sum == target :
            for k in range(i+1,j+1):
                sum = nums[i]+nums[k]
                if sum == target :
                    return [i,k]
            i+=1
        


        