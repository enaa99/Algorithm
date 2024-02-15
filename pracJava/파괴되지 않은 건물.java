class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        int m = board.length;
        int n = board[0].length;

        int[][] acc = new int[m+1][n+1];

        for(var s : skill){
            int degree = s[5];
            if(s[0] == 1){
                degree *= -1;
            }
            int y1 = s[1];
            int x1 = s[2];
            int y2 = s[3];
            int x2 = s[4];

            acc[y1][x1] += degree;
            acc[y1][x2+1] -= degree;
            acc[y2+1][x1] -= degree;
            acc[y2+1][x2+1] += degree;
        }

        for(int j = 0; j < m; j++){
            for(int i =1; i < n; i++){
                acc[j][i] += acc[j][i-1];
            }
        }


        for(int i = 0; i <n; i++){
            for(int j =1; j < m; j++){
                acc[j][i] += acc[j-1][i];
            }
        }

        for(int j = 0; j < m; j++){
            for(int i = 0; i < n; i++){
                board[j][i] += acc[j][i];
                if(board[j][i] > 0){
                    answer +=1;
                }
            }
        }


        return answer;
    }

    
}