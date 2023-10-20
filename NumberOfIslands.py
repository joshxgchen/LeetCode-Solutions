class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return False
        count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count+=1
                    self.dfs(grid, i, j) #mark
                        
        return count 
        
    def dfs(self, grid, i, j): #map it
        if i>=len(grid) or j>= len(grid[0]) or i<0 or j<0 or grid[i][j]=="0":
            return
        # check corners
        grid[i][j] = "0"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)
        
