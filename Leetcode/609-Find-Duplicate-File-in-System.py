from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dirs_dict = defaultdict(list)
        
        for dir_info in paths:
            dirs = dir_info.split(' ')
            root = dirs[0]
            for _dir in dirs[1:]:
                left_par, right_par = _dir.find('('), _dir.find(')')
                content = _dir[left_par + 1:right_par]    
                dirs_dict[content].append(root + '/' + _dir[:left_par])
        
        return [dirs for dirs in dirs_dict.values() if len(dirs) > 1]