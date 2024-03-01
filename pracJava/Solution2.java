import java.util.*;

public class Solution2 {
    public static void main(String[] args){
        
        Solution2 scheduler = new Solution2();
        int[] cores = {1, 2, 3};
        int n = 6;
        scheduler.solution(n, cores);
    }

    public int solution(int n, int[] cores) {
        int answer = 0;

        Queue<Integer> q = new LinkedList<>(); 

        int[] time = new int[cores.length];
        
        

        int minTime = cores[0]; 
        
        for (int i = 1; i < cores.length; i++) {
            if (cores[i] < minTime) {
                minTime = cores[i];
            }
            time[i] = cores[i];
        }

        for(int i = 0; i< n-cores.length; i++){
            q.offer(1);            
        }
        
        
        while(q.size() > 0){
            
            int nextMinTime = Integer.MAX_VALUE;

            for(int i = 0; i < cores.length; i++){
                int checkTime = time[i] - minTime;

                if(checkTime <= 0){
                    time[i] = cores[i];
                    answer = i;
                    nextMinTime = Math.min(nextMinTime, time[i]);
                    break;
                }
                else{
                    time[i] -= checkTime;
                    nextMinTime = Math.min(nextMinTime, time[i]);
                }
                
            }
            
            minTime = nextMinTime;
            
        }
        
        return answer;
    }
}
