public class RotateArray 
{

    public static int[] rotate(int arr[])
    {
        int n = arr.length;
        int t = arr[0];
        for (int i = 0; i < n - 1; i++)
        {
            arr[i] = arr[i + 1];
        }
        arr[n - 1] = t;
        return arr;
    }
    public static void main(String[] args) {
        int arr[] = {10, 20, 30, 40, 50, 60};
        arr = rotate(arr);
        for (int i : arr)
        {
            System.out.println(i);
        }
    }    
}
