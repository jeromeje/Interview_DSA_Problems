class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        start =0
        petrol = 0
        for i in range (0,len(gas)):
            petrol +=gas[i]
            petrol -= cost[i]
            if petrol <0:
                petrol =0 
                start = i+1   
        return start
