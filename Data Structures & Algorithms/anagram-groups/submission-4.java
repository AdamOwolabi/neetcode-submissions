class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> resDict = new HashMap<>(); 

        List<List<String>> res = new ArrayList<>();  

    

        for(int i = 0; i < strs.length; i++){
            char[] chars = strs[i].toCharArray(); 
            Arrays.sort(chars); 

            String sortedS = new String(chars);

            if(!(resDict.containsKey(sortedS))){
                resDict.put(sortedS, new ArrayList<>()); 
            }
                resDict.get(sortedS).add(strs[i]);
        }

        return new ArrayList<>(resDict.values());        
    }
}
