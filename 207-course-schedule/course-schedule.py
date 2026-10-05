class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        inDegree = [0 for _ in range(numCourses)]

        for to_take, pre_take in prerequisites:
            adj_list[pre_take].append(to_take)
            inDegree[to_take] += 1

        stack = []

        for i in range(numCourses):
            if inDegree[i] == 0:
                stack.append(i)
        count = 0
        while stack:
            node = stack.pop()
            count+=1
            for neighour in adj_list[node]:
                inDegree[neighour] -= 1
                if inDegree[neighour] == 0:
                    stack.append(neighour)

        return count == numCourses