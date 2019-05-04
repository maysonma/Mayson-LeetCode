class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return
            if rank[rootx] > rank[rooty]:
                parent[rooty] = rootx
            elif rank[rooty] > rank[rootx]:
                parent[rootx] = rooty
            else:
                parent[rootx] = rooty
                rank[rooty] += 1

        parent = list(range(len(accounts)))
        rank = [0] * len(accounts)
        email_parent = {}
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_parent:
                    union(idx, email_parent[email])
                email_parent[email] = idx
        ans = {}
        for email in email_parent:
            root = find(email_parent[email])
            if root in ans:
                ans[root].append(email)
            else:
                ans[root] = [accounts[root][0], email]
        ans = list(ans.values())
        for account in ans:
            account[1:] = sorted(account[1:])
        return ans
