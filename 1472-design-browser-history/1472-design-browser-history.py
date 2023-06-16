
class BrowserHistory(object):

    def __init__(self, homepage):
         self._history, self._future = [], []
        # 'homepage' is the first visited URL.
         self._current = homepage
        
    """
    :type homepage: str
    """
        

    def visit(self, url):
         # Push 'current' in 'history' stack and mark 'url' as 'current'.
        self._history.append(self._current)
        self._current = url
        # We need to delete all entries from 'future' stack.
        self._future = []
        
        """
        """
        

    def back(self, steps):
        # Pop elements from 'history' stack, and push elements in 'future' stack.
        while steps > 0 and self._history:
            self._future.append(self._current)
            self._current = self._history.pop()
            steps -= 1
        return self._current
        """

        :type steps: int
        :rtype: str
        """
        

    def forward(self, steps):
         # Pop elements from 'future' stack, and push elements in 'history' stack.
        while steps > 0 and self._future:
            self._history.append(self._current)
            self._current = self._future.pop()
            steps -= 1
        return self._current
        """
        :type steps: int
        :rtype: str
        """
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)