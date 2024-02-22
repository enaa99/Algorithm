class Solution {
    public int solution(int n, String control) {
        
        for(char i : control.toCharArray()){
            if(i == 'w'){
                n++;
            }
            else if(i == 's'){
                n--;
            }
            else if(i=='d'){
                n +=10;
            }
            else if(i == 'a'){
                n -=10;
            }
        }
        
        return n;
    }
}
