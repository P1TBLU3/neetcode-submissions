class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0)

        for index, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height_idx = stack.pop()
                height = heights[height_idx]
                
                left_wall = stack[-1] if stack else -1
                right_wall = index



                width = right_wall - left_wall - 1
                max_area = max(max_area, height * width)

            stack.append(index)
            
        return max_area