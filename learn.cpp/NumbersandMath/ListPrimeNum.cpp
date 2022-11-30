# include <iostream>
# include <cmath>

using namespace std;

int main() {

    int num = 0;

    cout<<"\nEnter a Number : ";    cin>>num;
    cout<<"\n";

    for (int i = 2; i < num; i++) 
    {
        bool prime = true;
        for (int j = 2; j*j <= i; j++) {
            if (i % j == 0) {
                prime=false;
                break;    
            }
        }   
        if(prime) cout << i <<", ";
    }
    
    cout<<"\n";

    return 0;
}