package PatternPrintingExamples;

import java.util.*;

public class HollowTriangle {

    public static void printHTriangle(int n) {

        for (int i=1; i<= n ; i++) {
            for (int j = i; j < n ; j++) {
                System.out.print(" ");
            }   
            for (int k = 1; k <= (2*i -1) ;k++) {
                if( k==1 || i == n || k==(2*i-1)) {
                    System.out.print("*");
                }
                else {
                    System.out.print(" ");
                }
            }
            System.out.println("");
        }
    }
    
    public static void main(String[] args) {

        int rows = 0;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of Rows: ");
        rows = input.nextInt();
        printHTriangle(rows);
        input.close();
    }
    
}
