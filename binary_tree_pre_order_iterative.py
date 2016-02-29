# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

result = []

def preorderTraversal(root, result):
    if root == None:
        return

    print (root.val)

    preorderTraversal(root.left, result)

    preorderTraversal(root.right, result)

    return

element1 = TreeNode(1)
element2 = TreeNode(2)
element3 = TreeNode(3)
element4 = TreeNode(4)

element5 = TreeNode(5)
element6 = TreeNode(6)
element7 = TreeNode(7)
element8 = TreeNode(8)

element9 = TreeNode(9)



element1.left = element2
element1.right = element3
element2.left = element4
element2.right = element7
element4.left = element5
element4.right = element6
element3.left = element8

element3.right = element9

preorderTraversal(element1, result)

result = []
elements = []

elements.append(element1)

while elements:
    curr_root = elements.pop(0)

    result.append(curr_root)

    if curr_root.right != None:
        elements.append(curr_root.right)

    if curr_root.left != None:
        elements.append(curr_root.left)

print "new result starts"
for each in result:
    print each.val

