def outNumber(e):
    return e['number']
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        conjunto = []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for place in counter:
            conjunto.append({'key': place, 'number': counter[place]})

        conjunto.sort(reverse=True, key=outNumber)
        output = []
        for i in range(k) :
            output.append(conjunto[i]['key'])
        return output