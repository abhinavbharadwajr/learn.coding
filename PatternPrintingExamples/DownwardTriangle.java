package PatternPrintingExamples;

import java.util.*;

public class DownwardTriangle
{
    public static void printDwnTriangle(int n) {

        System.out.println();                   // just to print a line after the user input
        for (int i=n-1; i>=0 ; i--) {
            for (int j=0; j<=i; j++) {
                System.out.print("*" + " ");
            }
            System.out.println();
        }
        System.out.println();                   // and to print a empty line of the pattern
    }
    public static void main(String[] args) {
        int rows;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of Rows : "); //takes input from user
        rows = input.nextInt();
        printDwnTriangle(rows);
        input.close();
    }
}