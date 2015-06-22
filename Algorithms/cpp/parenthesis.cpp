#include <iostream>
#include <string>
#include <stack>

using namespace std;

int balanced(string sentence)
{
	int i;
	char top;
	stack<char> s;
	for (i=0; i<sentence.length(); i++)
	{
		if (sentence[i] == '(')
		{
			s.push('(');
		}
		else if (sentence[i] == ')')
		{
			if (s.empty())
				return 0;
			top = s.top();
			s.pop();
			if (top != '(')
				return 0;
		}
	}
	return s.size() == 0;

}

int main(int argc, char ** argv)
{
	cout << balanced("(())") << endl;
 	cout << balanced("(()())") << endl;
 	cout << balanced("()(()())") << endl;
 	cout << balanced("(()") << endl;
 	cout << balanced("))") << endl;
	return 1;
}