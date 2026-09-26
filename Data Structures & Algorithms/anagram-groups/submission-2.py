class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #use the sorted, sort and rearrange, use as a key too
        res = []
        resDict = {}
        for s in strs: 
            sortedS = sorted(s) #this is a hash 
            if str(sortedS) not in resDict: 
                resDict[str(sortedS)] = [s] 
            else: 
                resDict[str(sortedS)].append(s)

        for k,v in resDict.items():
            res.append(v)

        return res