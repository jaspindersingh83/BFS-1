"""
Time: O(numCourses + prereqs)
Space: O(numCourses + prereqs)
Leet: Accepted
Problems: Didn't know Kahn's algorithm for topological sort. But understood it.
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses #maintain indegree of all courses

        for prereq in prerequisites:
            indegree[prereq[0]] += 1 #if there is a prereq increment indegree
        print("indegree"+str(indegree))

        queue = []
        for i in range(len(indegree)): #add to queue all nodes with indegree 0
            if indegree[i] == 0:
                indegree[i] -= 1 #reduce the indegree to -1 to signify that they are already added
                queue.append(i)
        visited = []
        while len(queue) != 0:
            curr = queue.pop(0) #pop off the nodes one by one
            visited.append(curr) #visit the node

            for prereq in prerequisites:
                if prereq[1] == curr: #update the prerequisites
                    indegree[prereq[0]] -= 1

            for i in range(len(indegree)):
                if indegree[i] == 0: #if all prereqs have been visited indegree will have reduced to zero
                    queue.append(i) #append such a node to queue
                    indegree[i] -= 1 #reduce indegree so it doesn't get appended again
        if len(visited) == numCourses:
            return True
        return False
