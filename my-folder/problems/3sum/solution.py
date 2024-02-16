class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        neg = defaultdict(int)
        pos = defaultdict(int)
        zeros = 0
        sol = []

        for x in nums:
            if x == 0:
                zeros+=1
            elif x > 0:
                pos[x] +=1
            else:
                neg[x] += 1
        if zeros > 0:
            for x in pos:
                if -x in neg:
                    sol.append( [0,x,-x])
            if zeros > 2:
                sol.append([0,0,0])
        for twofrom, onefrom in ((neg, pos), (pos, neg)):
            items_two = twofrom.items()
            for i, (key, value) in enumerate(items_two):
                for k2 in list(twofrom.keys())[i:]:
                    if -k2-key in onefrom and (k2 != key or value>1):
                        sol.append([k2, key, -k2-key])
                
        return sol

                