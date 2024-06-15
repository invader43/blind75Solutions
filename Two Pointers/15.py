class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # my idea is as follows 
        # [a,b,c,k,k,k,k]
        # 3 pointers , start at a,b,c 
        # shift c , shift b until it reaches left of c ,
        # shift c again
        # when c reaches end , do the same with a and b

        # the above idea is wrong since it requires you to keep track of unrepeated 
        # triplets in any order , meaning if [-1,0,1] is there , [0,-1,1] is not allowed


        nums = sorted(nums)

        i = 0 
        n = len(nums)
        threesum = []

        for i in range(n):
            if i>0 :
                if nums[i] == nums[i-1]:
                    continue
            
            #2sum implementation since nums[i+1:]
            j = i + 1
            k = n - 1
            while j < k :
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j +=1
                else :
                    threesum.append([nums[i],nums[j],nums[k]])
                    j += 1
                
                    while nums[j] == nums[j-1] and j < k :
                        j += 1


        return threesum

            

        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,0,1,2]
        # a = -4 , b = 