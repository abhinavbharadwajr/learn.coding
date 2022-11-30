package PatternPrinting;

import java.util.*;

public class RightTriangle {

    public static void rightTriangle(int n) 
    { 
        int i, j;  
        for(i=0; i<n; i++)                      //outer loop to print number of rows(n)
        {
            System.out.print(" ");              // line for printing space
            for(j=0; j<=i; ++j) {               // inner loop to print columns
                System.out.print("* ");         // print symbol
            }           
            System.out.println();               // ending line after each row
        }
        System.out.println();
    } 
    public static void main(String args[]) 
    { 
        int rows;
        Scanner input = new Scanner(System.in);
        System.out.println("\nEnter number of Rows : ");
        rows = input.nextInt();
        rightTriangle(rows);
        input.close(); 
    } 
    
}
