class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        minL = 0
        seen = set()
        if len(s) == 0:
            return 0

        for minR, letter in enumerate(s):
            while letter in seen:
                seen.remove(s[minL])
                minL+=1
            seen.add(letter)
            longest = max(longest, minR-minL+1)
        return longest

