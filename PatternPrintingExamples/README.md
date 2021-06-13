# User Input

**Optionally you can ask user to enter the symbol and make that symbol print too.**

**just add this code to the main program :**

```java 
String symbol = "";
System.out.println("\n Enter Symbol of your Choice : ");
symbol = input.next();
rightTriangle(rows, symbol);
```
**and modify the functionas as :**

###### Note : loop logic will vary with pattern! Please don't copy the same snippet below

```java
public static void <yourfunctionname> (int n, Sting sym) {
    for (int i=0; i<n; i++)                         //outer loop for number of rows(n)
        { 
            for (int j=n-i; j>1; j--) {             //inner loop for spaces
                System.out.print(" ");              //print space
            }  
            for (int j=0; j<=i; j++ ) {             //inner loop for number of columns
                System.out.print(sym);              //print symbol variable
            } 
            System.out.println();                   //ending line after each row
        }
        System.out.println();
}
```