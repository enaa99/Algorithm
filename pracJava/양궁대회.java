package Algorithm.pracJava;

import java.util.Arrays;

public class 양궁대회 {
    private static int[] answer;
    private static int result;

    public static void main(String[] args) {
        int[] info = {2,1,1,1,0,0,0,0,0,0,0};
        int[] result = solution(5, info);
        System.out.println(Arrays.toString(result));  // 결과 출력
    }

    public static int[] solution(int n, int[] info) {
        answer = new int[11];
        result = 0;
        dfs(10, n, new int[11]);
        return result != 0 ? answer : new int[]{-1};
    }

    private static int score(int[] ryan, int[] info) {
        int s = 0;
        for (int i = 0; i < 11; i++) {
            if (ryan[i] == 0 && info[i] == 0) continue;
            if (ryan[i] > info[i]) s += 10 - i;
            else s -= 10 - i;
        }
        return s;
    }

    private static void dfs(int idx, int left, int[] ryan) {
        if (idx == -1 || left < 0) return;
        if (left == 0) {
            int s = score(ryan, answer);
            if (result < s) {
                result = s;
                answer = ryan.clone();
            }
            return;
        }
        for (int i = left; i >= 0; i--) {
            ryan[idx] = i;
            dfs(idx - 1, left - i, ryan);
            ryan[idx] = 0;
        }
    }
}
