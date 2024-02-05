class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        String kk = Integer.toString(a) + Integer.toString(b);
        answer = 2*a*b;
        int cmp = Integer.parseInt(kk);
        
        if(cmp > answer){
            return cmp;
        }
        
        
        return answer;
    }
}