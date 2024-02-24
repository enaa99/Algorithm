import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] arr = new int[N];

        for(int i = 0; i < N; i ++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        br.close();

        int[] dp = new int[N];
        Arrays.fill(dp, 1);

        dp[0] = 1;
        for(int i = 1; i < N; i ++){
            for(int j = 0; j < i; j++){
                if(arr[j] < arr[i]){
                    dp[i] = Math.max(dp[i],dp[j]+1);
                }
            }
        }

        int max = -1;
        for (int i = 0; i < dp.length; i++) {
            if (dp[i] > max) {
                max = dp[i];
            }
        }
        System.out.println(max);
    }
}
