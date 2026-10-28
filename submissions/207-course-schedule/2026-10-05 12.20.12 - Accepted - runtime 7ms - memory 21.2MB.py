
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        predict={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            predict[crs].append(pre)
        visted=set()
        def dfs(crs):
            if crs in visted:
                return False
            if predict[crs]==[]:
                return True
            visted.add(crs)
            for i in predict[crs]:
                if not dfs(i): 
                    return False
            visted.remove(crs)
            predict[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True