class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        prefix = [0]*len(height)
        suffix = [0]*len(height)
        
        for i in range(len(height)):
            if i == 0:
                max_pr = height[i]
                max_aft = height[len(height) - 1 - i]
            else:
                 max_pr = max(max_pr,height[i])
                 prefix[i] = max_pr
                 max_aft = max(max_aft,height[len(height) - 1 - i])
                 suffix[len(height) - 1 - i] = max_aft

        total_water = 0

        for i in range(len(height)):
            water_added = min(prefix[i],suffix[i]) - height[i]
            total_water += max(0,water_added)
        
        return total_water