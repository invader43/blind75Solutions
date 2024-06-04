#contains duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for num in nums:
            if not num in mySet:
                mySet.add(num)
            else : return True
        
        return False