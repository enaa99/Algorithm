class Solution {
    public String solution(String my_string, int n) {
        StringBuilder answer = new StringBuilder();
        
        for(int i = 0; i < my_string.length(); i++){
            if(i == n){
                break;
            }
            answer.append(my_string.charAt(i));
        }
        
        return answer.toString();
    }
}