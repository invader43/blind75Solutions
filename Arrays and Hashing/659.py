class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for string in strs:
            l = len(string)
            s += "#" + str(l) + "#" + string
        
        return s

    def decode(self, s: str) -> List[str]:
        f = 0 #first hash
        t = 1 #second hash

        words = []
        while t <= len(s) - 1:
            if s[f] == "#":
                t = f + 1

                while not s[t] == "#":
                    t += 1
                
                l = s[f+1:t] # length 
                l = int(l)

                word = s[t+1:t+l+1]
                words.append(word)
                f = t+l+1

                if f >= len(s) - 1:
                    break

        return words