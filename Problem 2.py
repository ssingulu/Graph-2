# Time: O(V+E)
# Space: O(V+E)
class Solution(object):
    def __init__(self):
        self.cnt = 0
        self.mn = 100000000007
        self.saved = 0
        self.mx = 0
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        visited = [False]*len(graph)
        ans = 10000000007
        flag = True
        for i in range(len(initial)):
            if visited[initial[i]] == False:
                self.helper(initial[i], visited, graph, initial)
                #print(initial[i],self.saved)
                if self.cnt == 1 and self.mx < self.saved:
                    self.mx = self.saved
                    ans = initial[i]
                    flag = False

                elif self.cnt == 1 and self.mx == self.saved:
                    ans = min(ans, initial[i])
                    flag = False
                if flag:
                    ans = min(ans, self.mn)
            self.cnt = 0
            self.mn = 100000000007
            self.saved = 0
        return ans
                    
        
    def helper(self, node, visited, graph, initial):
        visited[node] = True
        self.saved += 1
        if node in initial:
            self.cnt += 1
            self.mn = min(self.mn, node)
        for i in range(len(graph)):
            if graph[node][i] == 1 and visited[i] == False:
                self.helper(i, visited, graph, initial)
        
        
        
        
