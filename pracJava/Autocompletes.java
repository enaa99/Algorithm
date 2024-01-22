package Algorithm.pracJava;

import java.util.HashMap;
import java.util.HashSet;
import java.util.*;

public class Autocompletes {
    
    public static int solution(String[] inputs) {
        
        Map<Character, Integer> inputDict = new HashMap<>();
        int count = 0;


        for(String i : inputs) {
            Set<Character> inputSet = new HashSet<>();

            for(char k : i.toCharArray()) {
                inputSet.add(k);
            }
            for(char j : inputSet) {
                if(inputDict.getOrDefault(j,0) == 0) {
                    inputDict.put(j, 1);
                }
                else{
                    count +=1;
                }
            }
        }

        return count;
    }

}
