#include <iostream>
#include <cmath>

using namespace std; // consider removing this line in serious projects

int main() {
	int num = 0;
	bool isPrime = true;

	cout<<"\nEnter a Number : "; cin>>num;

	if (num < 0) {
		cout<<"\n Unable to Determine the Result! Not a valid Input!";
	}
	else if (num == 0 || num == 1) {
		isPrime = false;
	}
	else {
		for (int i = 2; i < num; i++) {
        	if (num % i == 0)
            	isPrime = false;
		}
	}
	
	if(isPrime) {
		cout<<"\n"<<num<<" is a Prime Number!\n";
	}
	else {
		cout<<"\n"<<num<<" is not a Prime Number!\n";
	}

	return 0;
}