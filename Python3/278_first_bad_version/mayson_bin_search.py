# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def bin_search(l, r):
            while l != r:
                m = l + (r - l) // 2
                if isBadVersion(m):
                    r = m
                else:
                    l = m + 1
            return l
        return bin_search(1, n+1)