# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {}
        
        queue = collections.deque()
        queue.append([root, None])
        while queue:
            curr, parent = queue.popleft()
            parents[curr] = parent
            if curr.left: queue.append([curr.left, curr])
            if curr.right: queue.append([curr.right, curr])
        
        pparents = [p]
        ptemp = p
        while parents[ptemp]:
            pparents.append(parents[ptemp])
            ptemp = parents[ptemp]
        
        qparents = [q.val]
        qtemp = q
        while parents[qtemp]:
            qparents.append(parents[qtemp].val)
            qtemp = parents[qtemp]
            
        qparents.sort()
        for par in pparents:
            if self.binarySearch(qparents, par.val): return par
            
        return p
    
    def binarySearch(self, array, target):
        start = 0
        end = len(array) - 1
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                return True
            elif array[mid] > target:
                end = mid - 1
            else: start = mid + 1
        
        return False