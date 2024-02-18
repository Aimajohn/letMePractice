class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, maxl, counter = 0, len(s1), 0
        main = defaultdict(int)
        for l, n in enumerate(s1):
            main[s1[l]] = main.get(s1[l], 0) + 1 
        temp = defaultdict(int)
        for j, val in  enumerate(s2):
            temp[val]+=1
            counter+=1
            if counter > maxl:
                temp[s2[i]]-=1
                i+=1
                counter-=1
            if all([main[k] == temp[k] for k in main]):
                return True
        return False
            
            
