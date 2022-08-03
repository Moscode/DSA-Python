class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        What I learnt:
        (1) For a grid like problems, always look into using dictionary with property as tuple or set
        (2) Evaluate the appropriate data structure to use, 
            immediately after having an algo or approach before jumping into coding
        (3) Using defaultdict method from collections to avoid key error
        (4) Learnt about considering constrains when evaluating BIG O of an algorithms
        """
        store_for_row = collections.defaultdict(set)
        store_for_col = collections.defaultdict(set)
        sqrt = collections.defaultdict(set)
        
        #time complexity: O(1), space complexity: O(1)
        """
        Resources for why the Big O is constant even with two for loop and three dict:
        https://www.tutorialcup.com/interview/matrix/valid-sudoku.htm#Time_Complexity
        """
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] is not ".":

                    """Validate rows and columns"""
                    if (board[row][col] in store_for_row[row] or
                        board[row][col] in store_for_col[col]):
                        return False
                    store_for_col[col].add(board[row][col])
                    store_for_row[row].add(board[row][col])
                 
                    """Validate each square"""
                    if board[row][col] in sqrt[(row // 3, col // 3)]:
                        return False
                    sqrt[(row // 3, col // 3)].add(board[row][col])     
        return True
            