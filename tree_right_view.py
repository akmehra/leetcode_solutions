# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):

        temp = []

        result = []

        if root == None:
            return []

        temp.append(root)

        while temp:

            result.append(temp[len(temp)-1].val)

            temp1 = temp
            temp = []
            for i in range(len(temp1)):
                curr_root = temp1[i]

                if curr_root.left != None:
                    temp.append(curr_root.left)
                if curr_root.right != None:
                    temp.append(curr_root.right)

        return result