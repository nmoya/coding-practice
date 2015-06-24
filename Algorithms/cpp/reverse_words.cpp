#include <iostream>
#include <string>

using namespace std;

// message = 'find you will pain only go you recordings security the into if'

// reverse_words(message)
// # returns: 'if into the security recordings you go only pain will you find'

void reverse_characters(string &message, int start, int end)
{
	char tmp;

	while (start < end)
	{
		tmp = message[start];
		message[start] = message[end];
		message[end] = tmp;
		start++;
		end--;
	}
}

void reverse_words(string &message)
{
	int current_word = 0;
	reverse_characters(message, 0, message.length()-1);
	// Careful! Must be <= since the end parameter will be i-1
	for(int i=0; i<=message.length(); i++)
	{
		if (message[i] == ' ' || i == message.length())
		{
			reverse_characters(message, current_word, i-1);
			current_word = i+1;
		}
	}
}

int main(int argc, char **argv)
{
	string message = "find you will pain only go you recordings security the into if";
	cout << message << endl;
	reverse_words(message);
	cout << message << endl;
	return 1;
}