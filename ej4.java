public class ej4 {

    public static void main(String[] args) {
        String s = "";

        lengthOfLastWord(s);
    }

    public static int lengthOfLastWord(String s) {
        
        int length = 0;

        for (int i = s.length()-1; i >= 0; i--) {
            if(s.charAt(i)==' ' && length==0){
                continue;
            }else if (s.charAt(i)!=' ') {
                length++;
                continue;
            }
            return length;
        }
        return length;
    }
}