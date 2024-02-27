import java.util.*;
class Solution {
    public List<String> commonChars(String[] words) {
        ArrayList<String> arr = new ArrayList<>();

        HashMap<String,Integer> hsh = new HashMap<>();

        for(int i = 0; i < words[0].length(); i++){
            String key = String.valueOf(words[0].charAt(i));

            hsh.put(key, hsh.getOrDefault(key, 0) + 1);
        }


        for(int i = 1; i < words.length; i++){
            HashMap<String,Integer> hsh2 = new HashMap<>();

            for(char j : words[i].toCharArray()){
                hsh2.put(String.valueOf(j), hsh2.getOrDefault(String.valueOf(j), 0)+1);
            }
            
            for(String key : hsh.keySet()){

                int value = hsh2.getOrDefault(key, 0);
                if(value == 0){
                    hsh.put(key,0);
                }
                else{
                    hsh.put(key,Math.min(value, hsh.get(key)));
                }
            }

        }

        for(String key : hsh.keySet()){
            int v = hsh.get(key);
            if(v != 0){
                if(v > 1){
                    while(v-- > 0)
                        arr.add(key);
                }
                else{
                    arr.add(key);
                }
            }
        }

        return arr;
    }
}