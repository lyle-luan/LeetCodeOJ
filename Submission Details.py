# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        L = []
        sum = 0
        num = 0
        x = -1
        while root != None:
            if root.val != x:
                L.append(root)
                num = num*10 + root.val
                root.val = x
            if root.left != None and root.left.val != x:
                root = root.left
            elif root.right != None and root.right.val != x:
                root = root.right
            elif root.left == None and root.right == None:
                sum += num
                num = num/10
                del L[-1]
                if len(L) == 0:
                    break
                else:
                    root = L[-1]
            else:
                del L[-1]
                num = num/10
                if len(L) == 0:
                    break
                else:
                    root = L[-1]
        return sum
                
            