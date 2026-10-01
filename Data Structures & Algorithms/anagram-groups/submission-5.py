class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #use the sorted, sort and rearrange, use as a key too
        
        res = []
        resDict = {}

        for st in strs: 
            sortedS = str(sorted(st))
            if sortedS not in resDict: 
                resDict[sortedS] = [st]
            else: 
                resDict[sortedS].append(st)
        

        for k,v in resDict.items(): 
            res.append(v)
        
        return res
