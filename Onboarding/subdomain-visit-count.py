class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_domain = {}
    
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)
            subdomains = domain.split(".")
            
            for i in range(len(subdomains)):
                temp = ".".join(subdomains[i:])
                count_domain[temp] = count_domain.get(temp, 0) + count
        
        result = []
        
        for subdomain, count in count_domain.items():
            result.append(f"{count} {subdomain}")
        
        return result
            