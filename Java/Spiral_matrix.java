public class Spiral_matrix
{
    public static void main(String[] args) 
    {
        int arr[][] = {{1, 2, 3, 4}, 
                     {5, 6, 7, 8},
                     {9, 10, 11, 12}, 
                     {13, 14, 15, 16}};
        int row_min = 0;
        int row_max = arr.length - 1;
        int col_min = 0;
        int col_max = arr[0].length - 1;
        int steps = 0;

        while (steps < (arr.length * arr[0].length))
        {
            for (int i = col_min; i <= col_max; i++)
            {
                System.out.println(arr[row_min][i]);
                steps += 1;
            }
            row_min += 1;

            for (int i = row_min; i <= row_max; i++)
            {
                System.out.println(arr[i][col_max]);
                steps += 1;
            }
            col_max -= 1;

            for (int i = col_max; i >= col_min; i--)
            {
                System.out.println(arr[row_max][i]);
                steps += 1;
            }
            row_max -= 1;

            for (int i = row_max; i >= row_min; i--)
            {
                System.out.println(arr[i][col_min]);
                steps += 1;
            }
            col_min += 1;
        }
    }
}