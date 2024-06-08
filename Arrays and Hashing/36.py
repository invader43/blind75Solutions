class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Data structure used - hashset 
        hashset = set()

        #checking rows
        for i in range(9):
            for number in board[i][:]:
                print(number)
                if not number == ".":
                    if not number in hashset:
                        hashset.add(number)
                    else :
                        print('here') 
                        return False
            #resetting hashset
            hashset = set()   
        
        #checking columns
        for i in range(9):
            for j in range(9):
                number = board[j][i]
                print(number)
                if not number == ".":
                    if not number in hashset:
                        hashset.add(number)
                    else :
                        print('here') 
                        return False
            #resetting hashset
            hashset = set()

        #checking subboxes
        for i in range(3):
            for j in range(3):
                a = 3 * i
                b = 3 * j
                #(a,b) form the beginning index of each subgrid
                for m in range(3):
                    for n in range(3):
                        number = board[m+a][n+b]
                        print(number)
                        if not number == ".":
                            if not number in hashset:
                                hashset.add(number)
                            else :
                                print('here') 
                                return False
                #resetting hashset
                hashset = set()
        return True