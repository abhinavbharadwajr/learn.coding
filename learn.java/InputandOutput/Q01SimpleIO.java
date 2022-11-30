// package InputandOutput;

import java.util.Scanner;

public class Q01SimpleIO {
    public static void main(String[] args) {
        
        Scanner obj = new Scanner(System.in);
        
        /* uncomment the below line to have an
        Interactive Terminal for User Input */
        
        // System.out.println("\nYour Input : ");
        String userInput = obj.next();
        
        System.out.println(userInput);

        obj.close();
    }
}