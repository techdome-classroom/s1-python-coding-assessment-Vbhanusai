import deque
class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        ans=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='L':
                    ans+=1
                    queue=deque([(i,j)])
                    while queue:
                        x,y = queue.popleft()
                        if 0<=x<len(grid) and 0<=y<len(grid[0]):
                            grid[x][y]='W'
                            for dx,dy in dir:
                                queue.append((x+dx,y+dy))
        return 0
