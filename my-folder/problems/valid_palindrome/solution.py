class Solution:
    def isPalindrome(self, s: str) -> bool:
        todo = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        s = [letra for letra in s if letra in todo]
        t = s[::-1]
        return s == t
