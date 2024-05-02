public class reversearray 
{
    public static void main(String[] args) {
        int arr[] = {10, 20, 30, 40, 50, 60};
        int t, i = 0, j = arr.length - 1;

        /*for (int i = arr.length - 1; i >= 0; i--)
        {
            System.out.println(arr[i]);
        }
        */

        while (i < j)
        {
            t = arr[i];
            arr[i] = arr[j];
            arr[j] = t;
            i++;
            j--;
        }
        for (int k : arr)
        {
            System.out.println(k);
        }
    }
}
