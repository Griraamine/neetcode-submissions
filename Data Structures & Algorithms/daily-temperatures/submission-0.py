class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        stack = []
        result = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                tem , index = stack.pop()
                result[index] = i - index
            stack.append([t,i])
        return result 
        # use a stack , each time if the current is smaller than the elements in the stack , add the current 
        # if the current greater than the stack.head , pop until the stack.head is no longer less then current
        # at each pop action , we compute indice of stack.head - indice of current and store the difference in the indice of the stack.head




        