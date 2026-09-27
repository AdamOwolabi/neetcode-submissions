class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #use the sorted, sort and rearrange, use as a key too
        
        res = []
        resDict = {}

        for s in strs: 
            if str(sorted(s)) in resDict: 
                resDict[str(sorted(s))].append(s)
            else: 
                resDict[str(sorted(s))] = [s]

        
        for k,v in resDict.items():
            res.append(v)

        return res