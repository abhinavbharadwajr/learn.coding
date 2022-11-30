// package NumberPatterns;

import java.util.*;

public class SimpleNumPattern {

    public static void printNumPattern(int n) {

        int i, j,num; 
    
        for(i=0; i<n; i++) {                // outer loop for rows
            num=1; 
            for(j=0; j<=i; j++)             // inner loop for rows
            {
                System.out.print(num+ " "); // printing num with a space  
    
                num++;                      // incrementing value of num 
            }
            System.out.println();           // ending line after each row 
        }
    }
    
    public static void main(String[] args) {

        int rows = 0;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of Rows : ");
        rows = input.nextInt();
        printNumPattern(rows);
        input.close();
    }
}
