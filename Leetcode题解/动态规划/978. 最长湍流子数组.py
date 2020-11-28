class Solution:
    def maxTurbulenceSize(self, arr):
        # 长度小于等于1 直接返回1即可
        if len(arr) <= 1:
            return 1
        dp = [1] + [2]*(len(arr)-1)
        # 考虑到可能会有在1处断流， 加一个判断
        if arr[1] == arr[0]:
            dp[1] = 1
        # print(dp)
        for i in range(2, len(arr)):
            # 如果相等视为断流，dp[i] = 1
            if arr[i] == arr[i-1]:
                dp[i] = 1
            # 利用arr[i-1]与arr[i-2]判断前一个比较符号
            if arr[i-1] > arr[i-2]: 
                if arr[i] < arr[i-1]:
                    dp[i] = dp[i-1] + 1
            if arr[i-1] < arr[i-2]:
                if arr[i] > arr[i-1]:
                    dp[i] = dp[i-1] + 1
        return max(dp)

if __name__ == '__main__':
    s = Solution()
    maxTurbulenceSize1 = s.maxTurbulenceSize([9,4,2,10,7,8,8,1,9])
    maxTurbulenceSize2 = s.maxTurbulenceSize([4,8,12,16])
    print(maxTurbulenceSize1, maxTurbulenceSize2)
    
# 2020.11.28