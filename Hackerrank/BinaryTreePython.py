""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def isBST(root, min, max):
    if root == None: return True
    if root.data <= min or root.data >= max: return False
    else: return isBST(root.left, min, root.data) and isBST(root.right, root.data, max)

def check_binary_search_tree_(root):
    return isBST(root, -float("inf"), float("inf"))
