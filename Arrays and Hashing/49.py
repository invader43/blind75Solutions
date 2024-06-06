class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #datastructures used , array and hashmap
        sortedstrs = []
        hashmap = {}
        finallist = []

        #sort all individual strings
        for word in strs:
            sortedword = sorted(list(word))
            sortedstrs.append(''.join(sortedword))

        #now get indices that are equal , hashmap.get , and if it returns none , create a new key
        for i,srtedstr in enumerate(sortedstrs):
            if srtedstr in hashmap:
                hashmap[srtedstr].append(i)
            else :
                hashmap[srtedstr] = [i]

        #use keys and original list of strings to create the groups of anagrams
        for key in hashmap.keys():
            finallist.append([strs[i] for i in hashmap[key]])

        return finallist