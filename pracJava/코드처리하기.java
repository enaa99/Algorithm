class Solution {
    public String solution(String code) {
        StringBuilder answer = new StringBuilder();
        int mode = 0;
        for (int i = 0; i < code.length(); i++) {
            if (code.charAt(i) == '1') mode = 1 - mode;
            else if (i % 2 == mode) answer.append(code.charAt(i));
        }
        return "".equals(answer.toString()) ? "EMPTY" : answer.toString();
    }
}