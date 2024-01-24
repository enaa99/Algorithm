package Algorithm.pracJava;

class Solution {
    private static int[] answer;
    private static int result;
    
    public int[] solution(int n, int[] info) {
        answer = new int[11];
        result = 0;
        
        dfs(10, n ,new int[11], info);
        
        return result != 0 ? answer : new int[]{-1};
    }
    
    
    private static int score(int[] ryan, int[] info){
        int s =0;
        for(int i = 0; i<11; i++){
            if(ryan[i] == 0 && info[i] ==0) continue;
            if(ryan[i] > info[i]) s+=10-i;
            else s-= 10 - i;
        }
        return s;
    }
    
    private static void dfs(int idx, int left, int[] ryan, int[] info) {
        if(idx == -1 && left > 0 ) return;
        if(left ==0 ) {
            int s = score(ryan, info);
            if (result < s) {
                result = s;
                answer = ryan.clone();
            }
            return;
        }
        for(int i = left; i>=0; i--) {
            ryan[idx] = i;
            dfs(idx - 1, left - i, ryan, info);
            ryan[idx] = 0;
        }
    }
}