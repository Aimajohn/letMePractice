class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        deter = {}
        for i in range(len(s)):
            deter[s[i]] = deter.get(s[i], 0) + 1
        for j in range(len(t)):
            deter[t[j]] = deter.get(t[j], 0) - 1
        return ( all(deter.get(letter, 0) == 0 for letter in deter))
