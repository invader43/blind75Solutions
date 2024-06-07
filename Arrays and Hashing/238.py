class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix product problem 
        #data structure used - array
        pr_prod = []
        sf_prod = []
        ext_prod = []

        #creating prefix and suffix product
        for i,num in enumerate(nums) :
            j = len(nums) - i - 1 

            #prefix product , filled from start
            if i == 0:
                pr_prod.append(nums[0])
            else :
                pr_prod.append(nums[i]*pr_prod[i-1])
            
            #suffix product , filled from end
            if j == len(nums) - 1:
                sf_prod.insert(0,nums[j])
            else :
                sf_prod.insert(0,nums[j] * sf_prod[0])

        #using prefix and suffix product to get external product
        for i,num in enumerate(nums):
            if i == 0 :
                ext_prod.append(sf_prod[i+1])

            elif i == len(nums) - 1 :
                ext_prod.append(pr_prod[i-1])
            
            else :
                ext_prod.append(sf_prod[i+1] * pr_prod[i-1])

        return ext_prod