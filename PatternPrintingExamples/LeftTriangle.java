package PatternPrintingExamples;

import java.util.*;

public class LeftTriangle {

    public static void leftTriangle(int n) 
    { 
        int i, j;
        for(i=0; i<n; i++)                          // outer loop for number of rows(n)
        {
            for(j=2*(n-i); j>=0; j--) {              // inner loop for spaces 
                System.out.print(" ");              // printing space
            } 
            for(j=0; j<=i; j++) {                    // inner loop for columns
                System.out.print("* ");             // print star
            }           
            System.out.println();                   // ending line after each row
        }
        System.out.println(); 
    } 
    public static void main(String args[]) 
    { 
        int rows;
        Scanner input = new Scanner(System.in);
        System.out.println("\nEnter number of Rows : ");
        rows = input.nextInt();
        leftTriangle(rows);
        input.close(); 
    } 
    
}
