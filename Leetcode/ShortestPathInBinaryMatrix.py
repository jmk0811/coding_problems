class Solution:
    def isValid(self, cord, rowLen, colLen):
        return cord[0] >= 0 and cord[0] < rowLen and cord[1] >= 0 and cord[1] < colLen

    def isVisited(self, cord, visited):
        return visited[cord[0]][cord[1]]
    
    def getPath(self, prev, rowLen, colLen):
        curr = (rowLen - 1, colLen - 1)
        path = []
        step = 0
        while curr != (0, 0):
            step += 1
            path.append(curr)
            curr = prev[curr[0]][curr[1]]
        path.append((0, 1))
        
        return path[::-1]
    
    def BFS(self, grid) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        row = [-1, -1, 0, 1, 1, 1, 0, -1]
        col = [0, 1, 1, 1, 0, -1, -1, -1]
        visited = []
        queue = []
        prev = []

        for i in range(0, rowLen):
            visited.append([])
            prev.append([])
            for j in range(0, colLen):
                visited[i].append(False)
                prev[i].append(None)

        visited[0][0] = True
        queue.append((0, 0))

        while len(queue) != 0:
            curr = queue.pop(0)
            if grid[curr[0]][curr[1]] == 1: return -1
            if curr == (rowLen - 1, colLen - 1): return prev
            for i in range(0, 8):
                next = (curr[0] + row[i], curr[1] + col[i])
                if self.isValid(next, rowLen, colLen) and not self.isVisited(next, visited) and grid[next[0]][next[1]] == 0:
                    visited[next[0]][next[1]] = True
                    queue.append(next)
                    prev[next[0]][next[1]] = curr
                    
        return -1
    
    def shortestPathBinaryMatrix(self, grid) -> int:
        path = []
        res = self.BFS(grid)
        if res == -1: return -1
        else:
            path = self.getPath(res, len(grid), len(grid[0]))
            return len(path)