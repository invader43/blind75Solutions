class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 97 - 122 inclusive are the lowercase characters
        def cleanString(a):
            a = a.lower()
            # print(a)
            b = ''

            for _,c in enumerate(a) :
                # print(f'character - {c}')
                if ord(c) <= 122 and ord(c) >= 97:
                    b += c
                elif ord(c) <= 57 and ord(c) >= 48:
                    b += c
            # print(b)
            return b


        
        a = cleanString(s)
        for i,c in enumerate(a):
            j = len(a) - i - 1
            # print(i,j,a)
            if not a[i] == a[j]:
                return False

        return True

        # for cleaning string , ord() and chr() 


        # 1234321
        # racecar
        # 7
        # j = 6 , 5 , 4 , 3 , 2 , 1 , 0 


        # 1221
        # toot
        # 2

        # f(s) = int( len(s) / 2 )  

