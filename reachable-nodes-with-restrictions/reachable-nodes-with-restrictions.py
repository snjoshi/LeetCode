class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        seen=set()
        graph=collections.defaultdict(list)
        maxN=0
        ans=0

        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        #print(graph.items())
        
        def dfs(node):
            nonlocal maxN
            nonlocal ans
            for n in graph[node]:
                maxN=max(maxN,ans)
                if n not in seen:
                    seen.add(n)
                    ans+=1
                    dfs(n)


        seen.add(0)
        for i in restricted:
            seen.add(i)
        maxN,ans=1,1
        dfs(0)

        return maxN