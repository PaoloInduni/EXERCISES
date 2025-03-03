public class ej5 {
    public static void main(String[] args) {
        String[] strs = {"dog","racecar","car"};

        System.out.println(longestCommonPrefix(strs));
    }

    public static String longestCommonPrefix(String[] strs) {

        if (strs.length == 1) {
            return strs[0];
        }

        String prefix = "";
        

        for (int i = 0; i < strs[0].length(); i++) { // Recorremos cada letra de la primera palabra

            char letter = strs[0].charAt(i); // Escogemos la letra que está en la posición que queremos comparar

            for (String str : strs) { // Para cada string dentro del array

                if (i >= str.length()) { // Si no existe esa posición en la palabra a analizar

                    return prefix;

                }else if (str.charAt(i)!=letter) { // Si la letra en esa posición es distinta
                    return prefix;
                }
            }

            prefix += letter;
        }

        return prefix;
    }
}
