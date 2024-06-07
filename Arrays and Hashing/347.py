#Top k frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #most optimal way of traversing the nums list [1,1,1,2,2,3]
        # 1 - rank 1 
        # 1 - rank 1 - count 2
        # 1 - rank 1 - count 3
        # 1 - rank 1 - count 3 , 2 rank 2 - count 1
        # 1 - rank 1 - count 3 , 2 rank 2 - count 2
        # 1 - rank 1 - count 3 , 2 rank 2 - count 2 , 3 rank 3 - count 1
        #this can be achieved thru bucket sort with keys as counts of numbers
        # 1 , 2 , 3 , 4 , 5 , 6
        # 3 , 2 , 1 , None , None , None 
        
        #O(nlogn) solution 
        #hashmap solution with sorting ( bucket sort ill write after this)
        hashmap = {}


        worst_rank = 1 

        for num in nums:
            if not num in hashmap:
                hashmap[num] = 1 
            else :
                hashmap[num] += 1

        
        desc = sorted(hashmap.keys(),key = lambda x: hashmap[x],reverse = True)

        return desc[0:k]

            