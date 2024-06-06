class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #datastructures used , array and hashmap
        hashmap = {}
        finallist = []

        #sort individual strings
        for i,word in enumerate(strs):
            sortedword = sorted(list(word))
            sortedword = ''.join(sortedword)
        #now get indices that are equal , hashmap.get , and if it returns none , create a new key
            if sortedword in hashmap:
                hashmap[sortedword].append(i)
            else :
                hashmap[sortedword] = [i]

        #use keys and original list of strings to create the groups of anagrams
        for key in hashmap.keys():
            finallist.append([strs[i] for i in hashmap[key]])

        return finallist