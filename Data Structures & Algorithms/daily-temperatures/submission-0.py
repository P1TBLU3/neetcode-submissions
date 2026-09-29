class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            temp = temperatures[i]

            while stack and temp > temperatures[stack[-1]]:

                prev_i = stack.pop()
                dif = i-prev_i
                result[prev_i] = dif
            
            stack.append(i)

        return result



