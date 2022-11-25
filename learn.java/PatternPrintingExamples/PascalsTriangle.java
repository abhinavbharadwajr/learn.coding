package PatternPrintingExamples;

import java.util.*;

public class PascalsTriangle {
    
    public static void rPTriangle(int n) { // Function that prints Right Pascals Triangle

        // For the Top Half
        for (int i= 0; i<= n-1 ; i++)
        {
            for (int j=0; j<=i; j++) {
                System.out.print("*");
            }
            System.out.println("");
        }

        // For the Bottom Half
        for (int i=n-1; i>=0; i--) {
            for(int j=0; j <= i-1;j++) {
                System.out.print("*");
            }
            System.out.println("");
        }
    }

    public static void lPTriangle(int n) { // Functions that print Left Pascals Triangle

        // For the Top half
        for (int i=1; i<=n ; i++) {
            for (int j=i; j<n ;j++) {
                System.out.print(" ");
            }
            for (int k=1; k<=i;k++) {
                System.out.print("*");
            }
            System.out.println("");
        }

        // For the Bottom half
        for (int i=n; i>=1; i--) {
            for(int j=i; j<=n;j++) {
                System.out.print(" ");
            }
            for(int k=1; k<i ;k++) {
                System.out.print("*");
            }
            System.out.println(""); 
        }
    }

    public static void main(String[] args) {
    
        int rows = 0;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of rows: ");
        rows = input.nextInt();
        rPTriangle(rows);
        System.out.println("\n");
        lPTriangle(rows);
        input.close();
    }
}
