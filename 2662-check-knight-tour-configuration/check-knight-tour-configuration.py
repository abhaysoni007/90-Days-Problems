class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        rows, cols = len(grid), len(grid[0])
        if rows == cols == 1:
            return True
        pos = {}

        for i in range(rows):
            for j in range(cols):
                pos[grid[i][j]] = (i,j)
        count = 1
        last_pos = (0,0)
        while count < rows * cols:
            dx = pos[count][0] - last_pos[0]
            dy = pos[count][1] - last_pos[1]
            if not ((abs(dx) == 2 and abs(dy) == 1) or (abs(dx) == 1 and abs(dy) == 2)):
                return False

            last_pos = pos[count]
            count += 1
        
        return True