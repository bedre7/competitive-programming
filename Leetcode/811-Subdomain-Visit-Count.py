from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domaindict = defaultdict(int)
        
        for count_pair in cpdomains:
            count, root_domain = count_pair.split(' ')
            
            subdomain = root_domain
            while subdomain:
                domaindict[subdomain] += int(count)
                index = subdomain.find('.')
                if index != -1:
                    subdomain = subdomain[index + 1:]
                else:
                    break
        
        return [str(count) + " " + domain for domain, count in domaindict.items()]
            
        
        