# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append((root, 0))
        min_level = 0
        max_level = 0
        hash_map = defaultdict(list)
        result = []

        while queue:
            curr, level = queue.popleft()
            hash_map[level].append(curr.val)

            if curr.left:
                queue.append((curr.left, level - 1))
                min_level = min(min_level, level - 1)

            if curr.right:
                queue.append((curr.right, level + 1))
                max_level = max(max_level, level + 1)

        for i in range(min_level, max_level + 1):
            if i not in hash_map:
                continue

            result.append(hash_map[i])

        return result

