    class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
             return 1

        start = end = 0
        write = 0

        while end < len(chars):
            while chars[start] == chars[end]:
                end += 1
                    
            length = end - start
            if length == 1:
                chars[write] = chars[start]
                start += 1
                write += 1
            else:
                strLen = list(str(length)[::-1])
                chars[write] = chars[start]
                write += 1
                start += 1
                while strLen:
                    chars[write] = strLen.pop()
                    write += 1
                    start += 1
                start = end
        
        return write
            