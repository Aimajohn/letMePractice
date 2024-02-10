class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAn ={}
        for word in strs:
            added = False
            arranged = "".join(sorted(word))
            if(arranged in groupedAn):
                groupedAn[arranged].append(word)
            else:
                groupedAn[arranged] = [word]
        return groupedAn.values()