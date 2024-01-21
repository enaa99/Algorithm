package Algorithm.leetCode;

import java.util.*;
class Solution {
    public List<String> generateParenthesis(int n) {
        
        List<String> arr = new ArrayList<>();

        DFS(arr,1,0,n*2,"(");
        return arr;
    }



    private void DFS(List<String> arr, int l, int r, int len, String s) {
        if(s.length() == len) {
            arr.add(s);
            return;
        }

        if(l<len/2){
            DFS(arr,l+1,r,len,s+"(");
        }
        if(l>r){
            DFS(arr,l,r+1,len,s+")");
        }
    }
}