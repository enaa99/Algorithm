import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {

        ArrayList<Integer> arrList = new ArrayList<>();

        Map<Integer,Integer> answer = new HashMap<>(); 
        Map<Integer,Integer> arr2 = new HashMap<>(); 

        for(int i : nums1){
            answer.put(i, 0);
        }

        for(int i : nums2){
            arr2.put(i,0    );
        }

        if(answer.size() > arr2.size()){
            for(var key : answer.keySet()){

                int value = arr2.getOrDefault(key, -1);
                if(value != -1){
                    arrList.add(key);
                }
            }
        }
        else{
            for(var key : arr2.keySet()){

                int value = answer.getOrDefault(key, -1);
                if(value != -1){
                    arrList.add(key);
                }
            }
        }

        return arrList.stream().mapToInt(i->i).toArray();
    }

    public int[] intersection2(int[] nums1, int[] nums2) {

        int[] arr = new int[1001];
        for (int i : nums1) {
            arr[i] = 1;
        }

        int cnt = 0;
        for (int i : nums2) {
            if (arr[i] == 1) {
                arr[i] = 2;
                cnt++;
            }
        }
        
        int answer[] = new int[cnt];
        int j = 0;

        for (int i : nums2) {
            if (arr[i] == 2) {
                arr[i] = 1;
                answer[j++] = i;
            }
        }
        return answer;
    }
}



