#Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #datastructure used for problem
        hashmapS = {}
        hashmapT = {}

        #Initial Edge cases sorted 
        if not len(s) == len(t):
            return False

        #main logic - fill both hashmaps with character frequency 
        # then get one list of keys and compare counts
        #<code start here>
        for i,_ in enumerate(s):
            c1 = s[i]
            c2 = t[i]
            #has_key method for checking if the key already exists
            if c1 in hashmapS:
                hashmapS[c1] += 1 
            else : hashmapS[c1] = 1 

            if c2 in hashmapT:
                hashmapT[c2] += 1 
            else : hashmapT[c2] = 1 

        for key in hashmapT.keys() :
            #added .get instead of key lookup so keyError dont occur
            if not hashmapS.get(key) == hashmapT.get(key):
                return False

        return True

