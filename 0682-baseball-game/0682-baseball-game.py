class Solution(object):
    def calPoints(self, operations):
        score_stack = []
        
        for o in operations:
            if o == "+":
                score_stack.append(score_stack[-1] + score_stack[-2])
            elif o == "D":
                score_stack.append(2 * score_stack[-1])
            elif o == "C":
                score_stack.pop()
            else:
                score_stack.append(int(o))
        
        return sum(score_stack)
        """
        :type operations: List[str]
        :rtype: int
        """
        