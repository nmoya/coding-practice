#include <iostream>
#include <map>

using namespace std;

int main(int argc, char **argv)
{
	int i=0;
	int array[] = {1, 1, 1, 5, 5 ,5, 6, 6, 7, 8, 9, 1, 2, 3, 4, 1};
	map<int, int> hash;

	for (i=0; i <16; i++)
	{
		map<int, int>::iterator pointer = hash.find(array[i]);
		if (pointer == hash.end())
			hash[array[i]] = 1;
		else
			pointer->second++;
	}

	int max = -99999;
	int max_key = 0;
	for(map<int, int>::iterator i = hash.begin(); i != hash.end(); i++)
	{
		int key = i->first;
		if (hash[key] > max)
		{
			max = hash[key];
			max_key = key;
		}
	}
	cout << max_key << ":" << max << endl;

	return 1;
}