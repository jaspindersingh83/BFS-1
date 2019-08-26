"""
Time: O(n)
Space:O(n)
Leet: Accepted
Problems: None
"""

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def levelOrder(root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            if not root:
                return []

            result = []
            current_level = [root] #maintain current level
            real_nodes = 1

            while len(current_level) > 0:
                level = []
                for node in current_level:
                    level.append(node.val) #append each value of the current level into a list
                result.append(level) #append that list into the final list
                next_level = [] #using a for loop keep track of the next level
                for node in current_level:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                current_level = next_level #update

            return result

        levels = levelOrder(root) #stores output of level order traversal
        result = []
        for level in levels:
            result.append(level[-1]) #appends last element of each level to result
        return result
