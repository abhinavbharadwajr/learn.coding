package PatternPrintingExamples;

import java.util.*;

public class SandGalssPattern {
    
    public static void printSandGlass(int n) {

        // For loop that prints the Upper half 
        for (int i= 0; i<= n-1 ; i++) {
            for (int j=0; j <i; j++) {
                System.out.print(" ");
            }
            for (int k=i; k<=n-1; k++) {
                System.out.print("*" + " ");
            }
            System.out.println("");
        }
        
        // For loop that prints the Lower Half
        for (int i= n-1; i>= 0; i--) {
            for (int j=0; j< i ;j++) {
                System.out.print(" ");
            }
            for (int k=i; k<=n-1; k++)
            {
                System.out.print("*" + " ");
            }
            System.out.println("");
        }
    }

    public static void main(String[] args) {

        int rows =0;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of rows : ");
        rows = input.nextInt();
        printSandGlass(rows);
        input.close();
    }
}
