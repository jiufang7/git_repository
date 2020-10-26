class Solution:
    def minimumTotal(self, triangle) :
        # 相邻结点：与(i, j) 点相邻的结点为 (i + 1, j) 和 (i + 1, j + 1)。
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            #当我们在第i行的最左侧时，我们只能从第i−1行的最左侧移动。
            # 当j=i 时，f[i−1][j] 没有意义，因此状态转移方程为
            f[i][0] = f[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                f[i][j] = min(f[i-1][j-1], f[i-1][j]) + triangle[i][j]
            #最右侧的，只能从上一层的最右侧移动
            f[i][i] = f[i-1][i-1] + triangle[i][i]
        
        return min(f[n-1])
        '''
        空间复杂度为O(n)的解法，只用一维数组完成
        for i in range(1, n):
            f[i] = f[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                f[j] = min(f[j - 1], f[j]) + triangle[i][j]
            f[0] += triangle[i][0]

        return min(f)
        '''

# 2020.10.26
# 动态规划，杨辉三角的题目
# 只能用空间复杂度O(n^2)的，注释里有更省空间的办法