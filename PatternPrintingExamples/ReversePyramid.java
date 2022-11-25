package PatternPrintingExamples;

import java.util.*;

public class ReversePyramid {

    public static void rPyramid(int n) {
        for (int i= 0; i<= n-1 ; i++)
        {
            for (int j=0; j<=i; j++)
            {
                System.out.print(" ");
            }
            for (int k=0; k<=n-1-i; k++)
            {
                System.out.print("*" + " ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {

        int rows = 0;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of rows: ");
        rows = input.nextInt();
        rPyramid(rows);
        input.close();
    }
}
