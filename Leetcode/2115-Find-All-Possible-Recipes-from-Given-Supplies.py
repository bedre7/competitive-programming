class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for i, ings in enumerate(ingredients):
            for item in ings:
                adj[item].append(recipes[i])
                indegree[recipes[i]] += 1
        
        allRecipes = []
        queue = deque(supplies)
        while queue:
            supply = queue.popleft()
            for recipe in adj[supply]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)
                    allRecipes.append(recipe)
        
        return allRecipes