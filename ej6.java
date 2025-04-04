public class ej6 {

// Input: s = "a-bC-dEf-ghIj"
// Output: "j-Ih-gfE-dCba"

    public static void main(String[] args) {
        String s = "a-bC-dEf-ghIj";

        System.out.println(reverseOnlyLetters(s));
    }

    public static String reverseOnlyLetters(String s) {
        
        int l=0;
        int r=s.length()-1;
        char[] res=new char[r+1];

        while(l<=r){
            if(Character.isAlphabetic(s.charAt(l)) && Character.isAlphabetic(s.charAt(r))){
                res[r]=s.charAt(l);
                res[l]=s.charAt(r);
                l++;
                r--;
           }
          else if(!Character.isAlphabetic(s.charAt(r))){
                res[r]=s.charAt(r);
                r--;

          }
           else if(!Character.isAlphabetic(s.charAt(l))){
                res[l]=s.charAt(l);
                 l++;
             }
 }
        
        return new String(res);
    }
}
