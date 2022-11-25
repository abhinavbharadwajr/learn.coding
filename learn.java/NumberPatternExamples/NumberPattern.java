package NumberPatternExamples;

import java.util.*;

public class NumberPattern {
    
    public static void main(String[] args) {
        int i, j, k = 1;
        int rows;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of Rows : ");
        rows = input.nextInt();
        for (i = 1; i <= rows; i++) {
            for (j = 1; j< i + 1; j++) {
                System.out.print(k++ + " ");
            }
            System.out.println();
        }
    }
}
