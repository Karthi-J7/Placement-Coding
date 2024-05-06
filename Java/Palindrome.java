import java.util.Scanner;

public class Palindrome
{
    public static void main(String[] args) 
    {
        String s = new Scanner(System.in).next().toLowerCase();
        boolean key = true;
        for (int start = 0, end = s.length() - 1; start <= end; start++, end--)
        {
            if (s.charAt(start) != s.charAt(end))
            {
                key = false;
                break;
            }
        }        

        System.out.println(s + " is " + ( key ? "a " : "not a ") + "palindrome");
    }
}