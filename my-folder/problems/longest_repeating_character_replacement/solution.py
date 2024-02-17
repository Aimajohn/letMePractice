class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letras = defaultdict(int)
        left, longest, smax, right = 0, 0, 0, 0

        while right < len(s):
            letras[s[right]] +=1
            smax = max(smax, letras[s[right]])
            if right-left+1-smax > k:
                letras[s[left]]-=1
                left+=1
            else:
                longest = max(longest, right-left+1)
            right+=1
        
        return longest

