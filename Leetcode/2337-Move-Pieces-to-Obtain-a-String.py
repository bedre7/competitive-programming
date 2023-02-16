class Solution:
    def canChange(self, start: str, target: str) -> bool:
        sp = tp = 0
        s = list(start)
        t = list(target)
        reverse = False
        
        def skip():
            nonlocal sp, tp, reverse, t, s
            while s[sp] == '_' and 0 <= sp <= len(s):
                sp += -1 if reverse else 1
                if s[sp] == 'R':    
                    sp = len(s) - 1
                    reverse = True
                    skip()
                    break

            while t[tp] == '_' and 0 <= tp <= len(s):
                tp += 1 if not reverse else -1
                if t[tp] == 'R':
                    tp = len(t) - 1
                    reverse = True
        skip()
        
        while sp < len(s):
            if s[sp] != t[tp]:
                return False
            
            if sp == tp:
                skip()
                continue
            
            if s[sp] == 'L':
                while sp != 0 and s[sp - 1] == '_' and sp != tp:
                    s[sp], s[sp-1] = s[sp-1], s[sp]
                    sp -= 1
                    
            if s[sp] == 'R':
                while sp != len(s) and s[sp + 1] == '_' and sp != tp:
                    s[sp], s[sp+1] = s[sp+1], s[sp]
                    sp += 1
                if sp != tp: return False
            skip()
            print(sp, tp)
            # break
            
        return True

sol = Solution()
sol.canChange("_L__R__R_","L______RR")