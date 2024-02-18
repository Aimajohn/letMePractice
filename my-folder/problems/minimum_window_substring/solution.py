class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i, shortest = 0, len(s)
        sArray = []
        counter = 0
        temp, main = defaultdict(int),defaultdict(int)
        for letter in t:
            main[letter] = main.get(letter, 0)+1
        need = sum(main.values())
        actual = 0
        for j, n in enumerate(s):
            counter +=1
            temp[n] += 1
            if temp[n]<=main[n]:
                actual+=1
            while actual == need :
                if counter <= shortest:
                    shortest = counter
                    sArray = [i,j+1]
                temp[s[i]]-=1
                if temp[s[i]] < main[s[i]]:
                    actual-=1
                counter-=1
                i+=1
        return "" if sArray == [] else s[sArray[0]: sArray[1]]
