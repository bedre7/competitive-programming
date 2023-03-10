class Solution:
    def minOperations(self, logs: List[str]) -> int:
        self.files = []
        
        for log in logs:
            if log == '../':
                if self.files: self.files.pop()
            elif log == './':
                continue
            else:
                self.files.append(log[:-1])
        
        return len(self.files)