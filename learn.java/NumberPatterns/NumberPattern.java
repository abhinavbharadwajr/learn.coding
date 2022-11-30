// package NumberPatterns;

import java.util.*;

class NumberPattern {   
    public static void main(String[] args) {

        // Initializing requeired Variables
        int i, j, k = 1;
        int rows;
        
        // New Scanner Object for getting User Input
        Scanner input = new Scanner(System.in);
        System.out.println("\nEnter the number of Rows : ");
        rows = input.nextInt();

        // Loop to Print the Number Pattern
        System.out.println("\n");
        for (i = 1; i <= rows; i++) {
            for (j = 1; j< i + 1; j++) {
                System.out.print(k++ + " ");
            }
            System.out.println();
        }
    }
}
