# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dic = dict()
        self.res = []

        
        def putdic(value, key, key2):
            print(value, key)
            aux = self.dic.get(key, -1)
            if aux == -1:
                self.dic.update({key: {key2: [value]}})
            else:
                aux2 = aux.get(key2, -1)
                if aux2 == -1:
                    aux.update({key2: [value]})
                else:
                    aux2.append(value)
                    aux2.sort()
                    aux.update({key2: aux2})
                self.dic.update({key: aux})

        def per(node, i, j):
            if not node:
                return
            putdic(node.val, i, j)
            per(node.left, i-1, j+1)
            per(node.right, i+1, j+1)
        
        per(root, 0, 0)
        print(self.dic)
        for i in sorted(self.dic.keys()):
            aux = []
            getArray = self.dic.get(i).keys()
            for j in sorted(getArray):
                aux2 = self.dic.get(i).get(j)
                for k in aux2:
                    aux.append(k)
            self.res.append(aux)
        return self.res