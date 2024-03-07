class TimeMap:

    def __init__(self):
        self.opa = {
        }
    
    def sbi(self, times, target):
        i,j = 0, len(times)-1
        if target < times[0]:
            return -1
        if len(times) == 1:
            return 0
        while i<=j:
            val = (i+j)//2
            if times[val] == target:
                return val
            elif times[val] < target:
                i = val+1
            else:
                j = val-1
        return i-1

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.opa[key] =  self.opa.get(key, [[],[]])
        self.opa[key][0].append(value)
        self.opa[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        snums = self.opa.get(key, False)
        if not snums:
            return ""
        index = self.sbi(snums[1], timestamp)
        if index == -1:
            return ""
        return self.opa[key][0][index]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)