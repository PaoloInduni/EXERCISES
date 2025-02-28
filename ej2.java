public class ej2 {

    public static void main(String[] args) {
        int[] nums1 = { 2, 2, 3, 3, 3, 3, 2 };

        System.out.println(majorityElement(nums1));
    }

    public static int majorityElement(int[] nums) {

        int count = 0;
        int candidate = 0;
        
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            
            if (num == candidate) {
                count++;
            } else {
                count--;
            }
        }
        
        return candidate;
    }
}