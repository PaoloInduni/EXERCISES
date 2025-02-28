public class ej1 {

    // {1,2,3,0,0,0}

    public static void main(String Args[]) {

        int[] nums1 = { 0 };
        int[] nums2 = { 1 };

        int m = nums1.length;
        int n = nums2.length;

        merge(nums1, m, nums2, n);
    }

    public static void merge(int[] nums1, int m, int[] nums2, int n) {

        int indexN1 = m-1;
        int indexN2 = n-1;
        int pos = m+n-1;

        while (indexN2 >= 0) {
            if (indexN1 >= 0 && nums1[indexN1] > nums2[indexN2]) {
                nums1[pos] = nums1[indexN1];
                indexN1--;
            } else {
                nums1[pos] = nums2[indexN2];
                indexN2--;
            }
            pos--;
        }
    }
}