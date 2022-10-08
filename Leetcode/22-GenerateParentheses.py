class Par:
    def __init__(self, text, opens = 1, closes = 0):
        self.text = text
        self.opens = opens
        self.closes = closes
        
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        pars = [Par('(')]
        
        while True:
            i = 0
            appended = False
            if pars[i].opens < n:
                pars.append(Par(pars[i].text + '(', pars[i].opens + 1, pars[i].closes))
                appended = True
            if pars[i].closes < n and pars[i].closes < pars[i].opens:
                pars.append(Par(pars[i].text + ')', pars[i].opens, pars[i].closes + 1))
                appended = True
            if appended: pars.remove(pars[i])
            else: break
        
        return [p.text for p in pars]


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(3))