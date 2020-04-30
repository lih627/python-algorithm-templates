class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        minvalue = float('inf')
        ret = -1
        for idx in range(len(gas)):
            total += gas[idx] - cost[idx]
            if total < minvalue:
                ret = idx
                minvalue = total
        return (ret + 1) % len(gas) if total >= 0 else -1
