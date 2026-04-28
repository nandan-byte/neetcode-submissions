class Solution {
    public boolean isPalindrome(String s) {
        //TC - O(n)
        int i=0,
            j=s.length()-1;

        while(i < j){
            char l = s.charAt(i),
                 r = s.charAt(j);
            if(!Character.isLetterOrDigit(l)){
                i+=1;
                continue;
            }
            if(!Character.isLetterOrDigit(r)){
                j -=1;
                continue;
            }
            if(Character.toLowerCase(l) != Character.toLowerCase(r)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
