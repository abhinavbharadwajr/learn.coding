# include <iostream>
# include <string>
# include <cstring>

using namespace std;

string genFullName(string fName, string mName, string lName){
	
	if (islower(fName[0])) {
		fName[0] = toupper(fName[0]);
	}

	if (islower(mName[0])) {
		mName[0] = toupper(mName[0]);
	}

	if (islower(lName[0])) {
		lName[0] = toupper(lName[0]);
	}

	string flName = fName + " " + mName + " " + lName;
	return flName;
}

int main() {
	
	string firstName;
	string middleName;
	string lastName;
	int age;
	
	cout<<"\nEnter your First Name : ";	getline(cin, firstName);
	cout<<"\nEnter your Middle Name : ";	getline(cin, middleName);
	cout<<"\nEnter your Last Name : ";	getline(cin, lastName);
	cout<<"\nEnter you Age : ";		cin>>age;

	string fullName = genFullName(firstName, middleName, lastName);
	
	cout<<"\n"<<fullName<<" is "<<age<<" years Old.\n";

	return 0;
}

/*
O/P:
 
 Bro is 21.
*/