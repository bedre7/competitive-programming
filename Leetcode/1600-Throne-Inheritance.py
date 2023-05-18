from collections import defaultdict
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.throne = defaultdict(list)
        self.deadOnes = set()
        self.throne[kingName] = []

    def birth(self, parentName: str, childName: str) -> None:
        self.throne[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deadOnes.add(name)

    def getInheritanceOrder(self) -> List[str]:
        inheritance = []
        
        def dfs(parent):
            nonlocal inheritance
            if parent not in self.deadOnes:
                inheritance.append(parent)
                
            for child in self.throne[parent]:
                dfs(child)
                
        dfs(self.kingName)
        return inheritance


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()