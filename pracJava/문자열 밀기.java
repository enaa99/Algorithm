class Solution {
    public int solution(String A, String B) {
        int answer = 0;
        StringBuilder copy = new StringBuilder(A);
        
        int len = A.length();

        for (int i = 0; i < len; i++) {
            if (copy.toString().equals(B)) {
                return answer;
            }

            char k = copy.charAt(len-1);
            copy.deleteCharAt(len-1);
            copy.insert(0,k);
            answer++;
        }

        return -1;
    }
}