class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        input: array of integers -> represents the temp of each day
        output: array of integers, called 'result' -> represents the days required until 
        a  warmer temp day appears, 0 if none

        Questions:
        - can temperature be negative?: no
        - what should be returned when it's empty?: temp cannot be empty

        my approach:
        - you could just iterate through with O(n^2) time complexity
        - feels like a stack question
        - always decreasing stack

        using the example:
        input: [30,38,30,36,35,40,28]
        temp_output: [0,0,1,2,1,]
        output: []

        I think the info required would be in tuples: (value, index)
        
        pseudocode:

        # creating the stack
        stack = []
        
        take the current index and value and check if it is bigger than the top of stack
        if stack is empty, just add to stack
        else compare the top and current and subtract the indices
            pop the top of stack and try again

        above is iterated until the whole input array is seen, put 0 in remaining places



        """
        stack = []
        output = [0 for _ in range(len(temperatures))] # initializes list of 0s

        for index, value in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((index,value))
            else: #TODO might need to add loop
                while len(stack) > 0:
                    top = stack[-1]
                    if value <= top[1]:
                        break
                    else:
                        top_index, top_value = top
                        output[top_index] = index - top_index
                        stack.pop(-1)
                stack.append((index,value))

        return output



