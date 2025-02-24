# 36. Valid Sudoku

# Time Complexity: O(1)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

# Intuition:
# Use a set to store the numbers in the row, column, and box.
# If the number is already in the set, return False.
# Otherwise, add the number to the set and continue.
# Return True if the board is valid.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                k = i//3*3+j//3
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[k]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[k].add(board[i][j])
        return True
    
# Split checks - first check if the number is already in the set for a particular row, column, and box.
# Then add the number to the set after individual checks respectively.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rSet = [set() for _ in range(9)]
        cSet = [set() for _ in range(9)]
        bSet = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                current = board[i][j]

                if current != '.':
                    if current in rSet[i]:
                        return False

                    rSet[i].add(current)

                    if current in cSet[j]:
                        return False

                    cSet[j].add(current)

                    k = (i//3)*3 + (j//3)

                    if current in bSet[k]:
                        return False

                    bSet[k].add(current)

        return True

    