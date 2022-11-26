# include <iostream>
# include <stdlib.h>
# include <conio.h>

using namespace std;

int main () {

    int numone = 0, numtwo = 0;
    int sum = 0, diff = 0, prod = 0, div = 0;

    int uChoice = 0;
    char retry = 'y';
    
    cout<<"\nEnter Number One : ";  cin>>numone;
    cout<<"\nEnter Number Two : ";  cin>>numtwo;

    menu :

    cout<<"\n\t 1. Sum";
    cout<<"\n\t 2. Difference";
    cout<<"\n\t 3. Product";
    cout<<"\n\t 4. Division";

    cout<<"\n\n Enter your option : ";  cin>>uChoice;

    div = float(numone) / float(numtwo);

    switch(uChoice) {
        case 1 :
            sum = numone + numtwo;
            cout<<"\nSum of the Numbers : "<<sum<<"\n";
            break;
        
        case 2 :
            diff = numone - numtwo;
            cout<<"\nDifference of the Numbers : "<<diff<<"\n";
            break;

        case 3 :
            prod = numone * numtwo;
            cout<<"\nProduct of the Numbers: "<<prod<<"\n";
            break;
        
        case 4 :
            cout<<"\nDivision of the Numbers : "<<div<<"\n";
            break;
        
        default :
            cout<<"\n Not a Valid Option! Try again? (y / n): ";  cin>>retry;
            if (retry == 'y' || retry == 'Y') {
                goto menu;
            }
            else { break; }
    
    }

    return 0;
}