import sys
# s = {i for i in range(10)}
# print(s)
sys.path.append("./827_making_a_large_island")
from dfs_advanced_trick import Solution
s = Solution()
input0 = [[1, 0], [0, 1]]
print(s.largestIsland(input0))
