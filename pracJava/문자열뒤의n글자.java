class Solution {
    public String solution(String my_string, int n) {
        StringBuilder answer = new StringBuilder();
        
        int start = my_string.length() - n;
        
        for(int i = start; i < my_string.length(); i++){
            answer.append(my_string.charAt(i));
        }
        
        return answer.toString();
    }
}