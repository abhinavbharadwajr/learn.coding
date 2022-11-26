# include <iostream>
# include <stdlib.h>
# include <conio.h>

using namespace std;

/* Sum of Numbers with no Input from User

int main () {

	int a = 12;
	int b = 15;
	int sum = a + b;

	cout<<" Sum of Two Numbers is : "<<sum;

	return 0;
}

*/

void main()
{
	system("cls");

	int a = 0;	int b = 0;

	cout<<"\nEnter any Number : ";	cin>>a;
	cout<<"\nEnter another Number : ";	cin>>b;
	
	int sum = a + b;
	
	cout<<"\nSum of the given numbers : "<<sum<<"\n";
	
	getch();
}