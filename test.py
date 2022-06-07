class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    # TODO: Write your code here
    sum_all = 0
    cur_sum = 0

    def dfs(rt):
        nonlocal sum_all, cur_sum
        if rt is None:
            return

        cur_sum = cur_sum * 10 + rt.val
        print(cur_sum)

        if rt.left is None and rt.right is None:
            sum_all += cur_sum

        find_sum_of_path_numbers(rt.left)
        find_sum_of_path_numbers(rt.right)

        cur_sum = (cur_sum - rt.val) // 10

    dfs(root)

    return sum_all


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
