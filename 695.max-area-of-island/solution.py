class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0
        self.height = len(grid)
        self.width = len(grid[0])
        
        for y in range(self.height):
            for x in range(self.width):
                size = self.floodfill(grid, y, x)
                if size > max_size:
                    max_size = size
        
        return max_size
    
    def floodfill(self, grid, y, x):    
        if grid[y][x] == 1:
            grid[y][x] = 2
            size = 1
            if x < self.width -1:
                size += self.floodfill(grid, y, x+1)
            if x != 0:
                size += self.floodfill(grid, y, x-1)
            if y < self.height -1 :
                size += self.floodfill(grid, y+1, x)
            if y != 0:
                size += self.floodfill(grid, y-1, x)

            return size
        return 0
