import java.util.Arrays;

class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        
        return binarySearch(piles, h);
    }

    public int binarySearch(int[] piles, int h){

        Arrays.sort(piles);

        int left = 1;
        int right = piles[piles.length-1];

        while (left <right){
            int mid = left+(right-left)/2;
            if(check(piles, mid, h)){
                right = mid;
            }
            else{
                left = mid +1;
            }
        }

        return right;
    }


    public boolean check(int[] piles, int mid, int h){
        int count = 0;

        for(int v : piles){
            count += v/mid;
            if(v%mid != 0) count++;
        }
        
        return count <= h;
    }
}