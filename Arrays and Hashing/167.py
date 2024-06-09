#Two sum but sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since the array is sorted, using binary search to cut the search 
        #space after every failed.

        #data structure used - 2 pointers 
        l = 0
        r = len(numbers) - 1

        # while not numbers[l] + numbers[r] == target :
        #     if numbers[l] + numbers[int((l+r)/2)] < target :
        #         l = int((l+r)/2)
        #     else : r = int((l+r)/2)
        
        # return [l+1,r+1]

        #this solution is wrong since there is a possibility of missing the right answer
        #after every step 
        #eg 1,2,3,8,10,12,14,16 - 15 

        while not numbers[l] + numbers[r] == target :
            if l==r :
                return 0

            if  numbers[l] + numbers[r] > target :
                r = r - 1

            else : l = l + 1

        #[2,7,11,15] 2+15 = 17 , goal is 9
        # 7+15 = 22 , 2+11 = 13 , 13 is better shift r to l

        return [l+1,r+1]