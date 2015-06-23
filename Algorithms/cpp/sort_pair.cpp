#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Person
{
public:
	string name;
	int age;
	Person(string n, int a)
	{
		name = n;
		age = a;
	}
	~Person() {}
};

bool sort_by_age(const Person &A, const Person &B)
{
	return A.age < B.age;
}


int main(int argc, char **argv)
{
	vector<Person> V;
	V.push_back(Person("Nikolas", 72));
	V.push_back(Person("Thiago", 28));
	V.push_back(Person("Raphael", 25));

	sort(V.begin(), V.end(), sort_by_age);

	for(vector<Person>::iterator it = V.begin(); it != V.end(); ++it)
	{
		cout << it->name << " " << it->age << endl;
	}
}