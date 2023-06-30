class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen =set()
        ans=0
        graph=collections.defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            nonlocal ans
            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    dfs(n)
                    
        for x,y in edges:
            if x not in seen:
                ans+=1
                seen.add(x)
                dfs(x)

        for i in range(n):
            if i not in seen:
                ans+=1

        return ans
        