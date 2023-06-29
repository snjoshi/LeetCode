class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen=set()

        graph=collections.defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        
        def dfs(node):
            if node == destination:
                return True

            if node not in seen:
                seen.add(node)
                for n in graph[node]:
                    if dfs(n):
                        return True
            return False

        #seen.add(source)
        return dfs(source)


        