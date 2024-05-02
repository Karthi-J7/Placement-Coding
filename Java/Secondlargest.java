public class Secondlargest {
    public static void main(String[] args) {
        int[] arr = { 4, 2, 5, 4, 4, 2, 14, 2, 5, 4, 4, 2, 1 };
        int m1 = 0, m2 = -1;

        for (int i : arr) {
            if (i > m1) {
                m2 = m1;
                m1 = i;
            } 
            else if ((i < m1) && (i > m2)) {
                m2 = i;
            }
        }
        System.out.println("Second Largest: " + m2);
    }
}