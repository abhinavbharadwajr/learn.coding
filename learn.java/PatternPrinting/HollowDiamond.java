package PatternPrinting;

import java.util.*;

public class HollowDiamond {

    public static void printDiamond(int n) {

        for (int i=1; i<= n ; i++) {
            for (int j = n; j > i ; j--) {
            System.out.print(" ");
            }
            System.out.print("*");
            for (int k = 1; k < 2*(i -1) ;k++) {
                System.out.print(" ");
            }
            if(i==1) {
                System.out.println("");
            }
            else {
                System.out.println("*");
            }
        }
        
        for (int i=n-1; i>= 1 ; i--) {
            for (int j = n; j > i ; j--) {
                System.out.print(" ");
            }
            System.out.print("*");
            for (int k = 1; k < 2*(i -1) ;k++) {
                System.out.print(" ");
            }
            if( i==1)
                System.out.println("");
            else
                System.out.println("*");
        }
    }

    public static void main(String[] args) {

        int rows = 0;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of rows : ");
        rows = input.nextInt();
        printDiamond(rows);
        input.close();
    }
    
}
