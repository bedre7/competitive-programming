class Solution:
    def simplifyPath(self, path: str) -> str:
        files = path.split('/')
        canonical = []
        
        for file in files:
            if file == '' or file == '.':
                continue
            elif file == '..':
                if canonical: canonical.pop()
            else:
                canonical.append(file)
        
        return '/' + '/'.join(canonical)