class Solution:
    def makesquare(self, arr):
        if sum(arr) % 4:
            return False
        
        side = sum(arr) // 4
        n = len(arr)
        
        @lru_cache(None)
        def dp(mask, s):
            if mask == (1 << n) - 1:
                return True
            if not s:
                return dp(mask, side)
            
            for i in range(n):
                if mask & (1 << i) or s < arr[i]: continue
                if dp(mask ^ (1 << i), s - arr[i]):
                    return True
            return False
        
        return dp(0, side)





