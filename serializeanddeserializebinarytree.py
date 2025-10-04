# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity: O(n)
# Space Complexity: O(n)

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'

        # self.result=[]

        # def dfs(root):
        #     if root is None:
        #         self.result.append('null')
        #         return

        #     dfs(root.left)
        #     dfs(root.right)
        #     self.result.append(str(root.val))

        # dfs(root)
        # return ','.join(self.result)

        queue = deque()
        queue.append(root)
        result = []

        while queue:
            curr = queue.popleft()

            if curr:
                result.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                result.append('null')

        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == 'None':
            return None

        print(data)

        data_arr = data.split(',')
        idx = 0
        queue = deque()
        root = TreeNode(int(data_arr[idx]))
        queue.append(root)
        idx += 1

        while queue:
            curr = queue.popleft()

            if data_arr[idx] != 'null':
                curr.left = TreeNode(int(data_arr[idx]))
                queue.append(curr.left)
            idx += 1

            if data_arr[idx] != 'null':
                curr.right = TreeNode(int(data_arr[idx]))
                queue.append(curr.right)
            idx += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
