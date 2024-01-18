class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        mat3=[[0]*len(mat2[0]) for _ in range(len(mat1))]
        
        for r in range(len(mat1)):
            for c in range(len(mat2[0])):
                for k in range(len(mat2)):
                    mat3[r][c]+=mat1[r][k]*mat2[k][c]
                    
        return mat3
                
                
        