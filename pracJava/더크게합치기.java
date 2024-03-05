class Solution {
    public int solution(int a, int b) {
        
        String stringA = String.valueOf(a);
        String stringB = String.valueOf(b);
        
        return Math.max(Integer.parseInt(stringA + stringB), Integer.parseInt(stringB + stringA));
    }
}